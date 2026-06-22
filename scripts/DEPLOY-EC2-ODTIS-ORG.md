# Despliegue de ODTIS en [odtis.org](http://odtis.org)

Guía para publicar el sitio estático MkDocs en **tu EC2 existente** (donde ya corre `finnectos.com` con **Nginx + Cloudflare**).

**Tu configuración Cloudflare:** modo SSL **Flexible** (igual que `finnectos.com`).

Con **Flexible**, Cloudflare sirve HTTPS al visitante y se conecta al EC2 por **HTTP en puerto 80**. No hace falta certificado TLS en el origen ni `listen 443` en Nginx.

---

## Arquitectura

```text
Visitante ──HTTPS──► Cloudflare (SSL edge, modo Flexible)
│
└──HTTP:80──► EC2 Nginx ──► /var/www/odtis.org/
```


| Capa            | Rol                                                             |
| --------------- | --------------------------------------------------------------- |
| **Cloudflare**  | DNS, certificado público (edge), proxy - **SSL/TLS = Flexible** |
| **EC2 + Nginx** | `listen 80` por dominio (`finnectos.com` + `odtis.org`)         |
| **Tu Mac**      | `./scripts/build-site.sh` → `rsync`                             |


**MkDocs:** `site_url: https://odtis.org` en `site/mkdocs.yml` (ya configurado).

**No necesitas:** Certbot, Let's Encrypt ni Origin Certificate en el EC2.

---

## Checklist - primera vez

- [ ] **Cloudflare DNS:** `@` y `www` → IP del EC2, proxy **on** (nube naranja)
- [ ] **Cloudflare SSL/TLS:** modo **Flexible** en la zona `odtis.org` (igual que finnectos)
- [ ] **EC2:** `/var/www/odtis.org` creado
- [ ] **Nginx:** vhost `odtis.org` con **solo** `listen 80` (sin bloque SSL)
- [ ] `sudo nginx -t && sudo systemctl reload nginx`
- [ ] **Build + rsync**
- [ ] [https://odtis.org](https://odtis.org) OK; finnectos.com sigue OK

---

## 1. Cloudflare - DNS

Dashboard → **DNS → Records** (zona `odtis.org`):


| Type      | Name  | Content                              | Proxy   |
| --------- | ----- | ------------------------------------ | ------- |
| **A**     | `@`   | IP pública del EC2 (la de finnectos) | Proxied |
| **CNAME** | `www` | `odtis.org`                          | Proxied |


**Comprobar:** el registro A en el dashboard muestra tu IP de origen. Con proxy activo, `dig odtis.org` puede devolver IPs de Cloudflare; es normal.

---

## 2. Cloudflare - SSL modo Flexible

**SSL/TLS → Overview → Flexible** (misma opción que `finnectos.com`).


| Tramo                     | Protocolo            |
| ------------------------- | -------------------- |
| Visitante → Cloudflare    | HTTPS                |
| Cloudflare → EC2 (origen) | **HTTP (puerto 80)** |


**En Nginx para odtis.org:**

- `listen 80;` - sí
- `listen 443 ssl;` - **no** (no lo necesitas con Flexible)
- Certificado en el EC2 - **no**

Replica el patrón de finnectos:

```bash
sudo grep -E 'server_name|listen' /etc/nginx/sites-enabled/*
```

El vhost de `finnectos.com` debería tener solo `listen 80`. Haz lo mismo para `odtis.org`.

### Redirect www → apex (opcional)

Cloudflare → **Rules → Redirect Rules:** `www.odtis.org/*` → `https://odtis.org/$1` (301).

---

## 3. EC2 - docroot y permisos

Amazon Linux usa `**ec2-user`**. El docroot debe ser escribible por quien hace `rsync`:

```bash
ssh -i ~/.ssh/your-deploy-key.pem ec2-user@TU_IP_EC2

sudo mkdir -p /var/www/odtis.org
sudo chown -R ec2-user:ec2-user /var/www/odtis.org
sudo chmod 755 /var/www/odtis.org
```

Comprueba:

```bash
ls -la /var/www/ | grep odtis
# drwxr-xr-x ... ec2-user ec2-user ... odtis.org
```

> **Error rsync `Permission denied`:** el directorio lo creó `root` con `sudo mkdir` sin `chown`. Ejecuta `sudo chown -R ec2-user:ec2-user /var/www/odtis.org` y repite el `rsync`.

Tras un `rsync` correcto, Nginx (usuario `nginx`) debe poder **leer** los archivos:

```bash
# En el EC2, después del rsync
sudo find /var/www/odtis.org -type d -exec chmod 755 {} \;
sudo find /var/www/odtis.org -type f -exec chmod 644 {} \;

# Amazon Linux: SELinux puede causar 403 aunque exista index.html
sudo chcon -R -t httpd_sys_content_t /var/www/odtis.org 2>/dev/null || true
```

Comprueba que hay contenido:

```bash
ls -la /var/www/odtis.org/index.html
ls /var/www/odtis.org/ | head
```

---

## 4. EC2 - vhost Nginx (solo HTTP / puerto 80)

Plantilla: `[nginx-odtis.org.conf](nginx-odtis.org.conf)` - un solo bloque `listen 80`, sin SSL.

### 4.1 Subir la plantilla

```bash
# Desde tu Mac (Amazon Linux → ec2-user)
scp -i ~/.ssh/your-deploy-key.pem \
odtis/scripts/nginx-odtis.org.conf \
ec2-user@TU_IP_EC2:/tmp/odtis.org.conf
```

En el EC2, **comprueba que el archivo llegó**:

```bash
ls -la /tmp/odtis.org.conf
```

Si no existe, el `scp` falló (clave, IP, usuario `ubuntu` vs `ec2-user`).

### 4.2 Dónde poner el vhost (depende del SO)

**Amazon Linux / RHEL** no usan `sites-available/` - suelen usar `**/etc/nginx/conf.d/`**.

Mira dónde está la config de finnectos:

```bash
sudo nginx -T 2>/dev/null | grep -E 'server_name|include' | head -20
ls -la /etc/nginx/sites-available/ 2>/dev/null || echo "no sites-available"
ls -la /etc/nginx/conf.d/
```


| Si ves…                                                              | Comando de instalación |
| -------------------------------------------------------------------- | ---------------------- |
| Carpeta `**/etc/nginx/conf.d/**` (typical Amazon Linux)              | Ver **Opción A**       |
| Carpetas `**sites-available`** + `**sites-enabled**` (Ubuntu/Debian) | Ver **Opción B**       |


**Opción A - `conf.d/` (Amazon Linux, etc.)**

```bash
sudo cp /tmp/odtis.org.conf /etc/nginx/conf.d/odtis.org.conf
sudo nginx -t
sudo systemctl reload nginx
```

**Opción B - `sites-available` (Ubuntu/Debian)**

Si `sites-available` no existe, créala:

```bash
sudo mkdir -p /etc/nginx/sites-available /etc/nginx/sites-enabled
grep -q 'sites-enabled' /etc/nginx/nginx.conf || \
echo 'include /etc/nginx/sites-enabled/*;' | sudo tee /etc/nginx/conf.d/sites-enabled.conf
```

Instala el vhost:

```bash
sudo cp /tmp/odtis.org.conf /etc/nginx/sites-available/odtis.org
sudo ln -sf /etc/nginx/sites-available/odtis.org /etc/nginx/sites-enabled/odtis.org
sudo nginx -t
sudo systemctl reload nginx
```

> **Error `mv: ... No such file or directory`:** casi siempre falta el directorio destino (`sites-available` no existe en tu AMI). Usa **Opción A** o crea las carpetas en **Opción B**. Preferible `cp` en lugar de `mv` por si quieres conservar `/tmp/odtis.org.conf`.

**Importante:**

- No toques el vhost de `finnectos.com`.
- `server_name odtis.org www.odtis.org;` y `root /var/www/odtis.org;` exclusivos de ODTIS.
- MkDocs requiere `try_files $uri $uri/ $uri/index.html =404;` (incluido en la plantilla).

Prueba en el servidor:

```bash
curl -sI -H "Host: odtis.org" http://127.0.0.1/ | head -3
curl -sI -H "Host: finnectos.com" http://127.0.0.1/ | head -3
```

---

## 5. Build y deploy

### Primera vez (venv local)

```bash
cd odtis
python3 -m venv .venv-site
source .venv-site/bin/activate
pip install -r site/requirements.txt
```

### Deploy rutinario (un solo comando)

Configura **una vez**:

```bash
cp scripts/odtis-deploy.env.example scripts/odtis-deploy.env
# edita ODTIS_EC2_HOST y ODTIS_SSH_KEY si hace falta
```

Cada publicación:

```bash
cd odtis
./scripts/deploy-ec2.sh
```

El script hace: **build** → **rsync** → **permisos nginx/SELinux** en el EC2.

Opciones:

```bash
./scripts/deploy-ec2.sh --skip-build   # solo rsync (build ya hecho)
./scripts/deploy-ec2.sh --skip-fix     # sin chmod/chcon remoto
```

Alternativa: variables en `~/.odtis-deploy.env` (mismas claves que `scripts/odtis-deploy.env`).

### Deploy manual (equivalente)

```bash
cd odtis && ./scripts/build-site.sh
rsync -avz --delete \
-e "ssh -i $ODTIS_SSH_KEY" \
../build/odtis-spec-site/ \
"$ODTIS_EC2_HOST:/var/www/odtis.org/"

# Permisos lectura para nginx (ejecutar en EC2 o por SSH remoto)
ssh -i "$ODTIS_SSH_KEY" "$ODTIS_EC2_HOST" \
'sudo find /var/www/odtis.org -type d -exec chmod 755 {} \; && \
sudo find /var/www/odtis.org -type f -exec chmod 644 {} \; && \
sudo chcon -R -t httpd_sys_content_t /var/www/odtis.org 2>/dev/null || true'
```

Preview local: `mkdocs serve -f site/mkdocs.yml` → [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 6. Verificación


| Paso                           | Comando / URL                                      |
| ------------------------------ | -------------------------------------------------- |
| Archivos                       | `ls /var/www/odtis.org/index.html`                 |
| Origen HTTP                    | `curl -sI -H "Host: odtis.org" http://127.0.0.1/`  |
| Público (HTTPS vía Cloudflare) | [https://odtis.org](https://odtis.org)             |
| Rutas MkDocs                   | `/spec/`, `/conformance/`                          |
| finnectos                      | [https://finnectos.com](https://finnectos.com)     |
| Caché                          | Cloudflare → **Caching → Purge** si no ves cambios |


---

## Errores frecuentes (modo Flexible)


| Síntoma                                           | Causa                                                   | Solución                                                            |
| ------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------------------- |
| **522**                                           | Origen no responde / SG cierra **80**                   | Abre puerto **80** en security group; `systemctl status nginx`      |
| **525**                                           | Nginx solo en 443 sin cert válido                       | Con Flexible usa **solo puerto 80**; quita bloques `listen 443 ssl` |
| **404** en rutas                                  | Falta `try_files`                                       | Usar `[nginx-odtis.org.conf](nginx-odtis.org.conf)`                 |
| **403 Forbidden**                                 | Carpeta vacía (rsync falló) o nginx/SELinux sin lectura | Ver sección 7 abajo                                                 |
| `**Permission denied` en rsync**                  | `/var/www/odtis.org` es de `root`                       | `sudo chown -R ec2-user:ec2-user /var/www/odtis.org`                |
| `**mv: No such file or directory`**               | No existe `sites-available/` (Amazon Linux)             | Usar `/etc/nginx/conf.d/odtis.org.conf` (sección 4.2)               |
| finnectos roto                                    | Vhost sobrescrito                                       | Un archivo por dominio; restaurar backup                            |
| Página vieja                                      | Caché Cloudflare                                        | Purge cache                                                         |
| Enlaces mal dominio                               | Build sin `site_url`                                    | `https://odtis.org` en `mkdocs.yml` + rebuild                       |
| **curl 200 en EC2, navegador no carga**           | DNS / Cloudflare / NS del registrar                     | Sección 8                                                           |
| **"The content cannot be displayed"** + SSL error | NS aún en Namecheap → parking (`192.64.x.x`)            | Sección 8 - NS no migrados                                          |


---

## 7. Diagnóstico: 403 y carpeta vacía

Si `ls /var/www/odtis.org/index.html` falla **y** `curl` devuelve **403**:

1. **No hay sitio desplegado** (el rsync anterior falló por permisos).
2. Nginx sí reconoce el vhost `odtis.org` (por eso responde 403, no 404 de otro sitio).

### Paso A - permisos para rsync (EC2)

```bash
sudo chown -R ec2-user:ec2-user /var/www/odtis.org
ls -la /var/www/ | grep odtis
```

### Paso B - build + rsync (Mac)

```bash
cd /path/to/core-spec
./scripts/build-site.sh

rsync -avz --delete \
-e "ssh -i ~/.ssh/your-deploy-key.pem" \
../build/odtis-spec-site/ \
ec2-user@YOUR_EC2_PUBLIC_IP:/var/www/odtis.org/
```

Debe terminar **sin** `Permission denied`. Deberías ver ~370 archivos transferidos.

### Paso C - permisos lectura nginx + SELinux (EC2)

```bash
sudo find /var/www/odtis.org -type d -exec chmod 755 {} \;
sudo find /var/www/odtis.org -type f -exec chmod 644 {} \;
sudo chcon -R -t httpd_sys_content_t /var/www/odtis.org
```

### Paso D - verificar vhost apunta al docroot correcto

```bash
sudo nginx -T 2>/dev/null | grep -A5 'server_name odtis.org'
# root debe ser /var/www/odtis.org;
```

### Paso E - probar de nuevo

```bash
ls -la /var/www/odtis.org/index.html
curl -sI -H "Host: odtis.org" http://127.0.0.1/ | head -5
# HTTP/1.1 200 OK
```

---

## 8. Diagnóstico: curl 200 en el servidor pero el navegador no carga

Si en el EC2:

```bash
curl -sI -H "Host: odtis.org" http://127.0.0.1/ # → 200 OK
```

pero **[https://odtis.org](https://odtis.org)** en el navegador no carga, el origen (Nginx + archivos) está bien. El fallo está en **DNS o Cloudflare** (camino Internet → Cloudflare → EC2).

### Desde tu Mac

```bash
# ¿Resuelve el dominio?
dig odtis.org +short
dig www.odtis.org +short

# ¿Apunta a Cloudflare o está vacío?
dig odtis.org NS +short

# Prueba HTTPS pública
curl -sI --max-time 10 https://odtis.org | head -10
curl -sI --max-time 10 http://odtis.org | head -10

# Prueba IP directa (bypass DNS) - debe dar 200 si Nginx está bien
curl -sI --max-time 10 -H "Host: odtis.org" http://YOUR_EC2_PUBLIC_IP/ | head -5
```


| Resultado                                                           | Significado                                             | Acción                                                     |
| ------------------------------------------------------------------- | ------------------------------------------------------- | ---------------------------------------------------------- |
| `dig odtis.org` **vacío** o IP incorrecta                           | DNS no configurado o NS del registrar no son Cloudflare | Ver checklist Cloudflare abajo                             |
| `dig` devuelve IPs **104.x / 172.x** (Cloudflare)                   | DNS edge OK                                             | Revisar registro A en dashboard (IP origen) y SSL Flexible |
| `curl https://odtis.org` **timeout / no resuelve**                  | DNS o zona inactiva en Cloudflare                       | Añadir sitio en Cloudflare; cambiar NS en Namecheap        |
| `curl` a IP directa con `Host: odtis.org` → **200** pero dominio no | Solo falla DNS/Cloudflare                               | Arreglar registros en Cloudflare                           |
| **522** en navegador                                                | Cloudflare no alcanza el EC2                            | Security group puerto **80**; Nginx activo                 |
| **525 / 526**                                                       | Modo SSL distinto a Flexible                            | SSL/TLS → **Flexible** en zona `odtis.org`                 |


### Checklist Cloudflare (zona `odtis.org`)

1. **Websites** → `odtis.org` aparece como **Active** (no solo `finnectos.com`).
2. En el **registrar** (Namecheap): nameservers = los de Cloudflare (`*.ns.cloudflare.com`).
3. **DNS → Records:**

- `A` `@` → `YOUR_EC2_PUBLIC_IP` (tu IP EC2) - **Proxied** (nube naranja)
- `CNAME` `www` → `odtis.org` - Proxied

1. **SSL/TLS → Overview → Flexible** (igual que finnectos).
2. Sin registro `AAAA` roto apuntando a otra IP.
3. **SSL/TLS → Edge Certificates:** certificado activo para `odtis.org` (suele generarse en minutos).

### Señal de que los NS NO están en Cloudflare (tu caso típico)

```bash
dig odtis.org NS +short
# MAL: dns1.registrar-servers.com / dns2.registrar-servers.com (Namecheap)

dig odtis.org +short
# MAL: 192.64.119.26 (parking Namecheap - no es tu EC2 ni Cloudflare)
```

Mientras veas `registrar-servers.com`, **Cloudflare no recibe tráfico**: las reglas de redirect/HTTPS en Cloudflare **no hacen nada**. El navegador va al parking de Namecheap y falla el SSL → *"The content of the page cannot be displayed"*.

**BIEN** cuando:

```bash
dig odtis.org NS +short
# ada.ns.cloudflare.com
# bob.ns.cloudflare.com (tus NS reales)

dig odtis.org +short
# 104.x.x.x o 172.x.x.x (IPs Cloudflare, proxy on)
```

### Arreglar nameservers en Namecheap (paso a paso)

1. Cloudflare → sitio **odtis.org** → copia los **2 nameservers** exactos (Overview).
2. Namecheap → **Domain List** → `odtis.org` → **Manage**.
3. Sección **Nameservers** → elige **Custom DNS** (no "Namecheap BasicDNS").
4. Pega los 2 NS de Cloudflare → **Save** (checkmark verde).
5. Espera 15-60 min; comprueba hasta que `dig odtis.org NS +short` muestre `*.cloudflare.com`.

Errores frecuentes en Namecheap:

- Guardar NS en otro dominio por error.
- Dejar **BasicDNS** activo (sigue usando `registrar-servers.com`).
- Configurar DNS en Namecheap **Advanced DNS** pero NS ya apuntan a Cloudflare (esos registros se ignoran; edita solo en Cloudflare).

### Cuando Cloudflare ya esté activo

1. **DNS → Records:** `A` `@` → `YOUR_EC2_PUBLIC_IP` Proxied; `CNAME` `www` → `odtis.org` Proxied.
2. **SSL/TLS → Overview → Flexible**.
3. **SSL/TLS → Edge Certificates → Always Use HTTPS** = ON (no hace falta Redirect Rule para esto).
4. Elimina reglas **Redirect Rules** de prueba si causan bucles.
5. Borra registros **AAAA** si el EC2 no tiene IPv6.
6. **Caching → Purge Everything** tras el primer deploy.

### Atajo si no quieres esperar propagación NS

Quedarte en **Namecheap BasicDNS** (sin Cloudflare por ahora):

1. Namecheap → Advanced DNS → quita **URL Redirect Record** / parking.
2. `A` `@` → `YOUR_EC2_PUBLIC_IP`.
3. `A` o CNAME `www` → `YOUR_EC2_PUBLIC_IP` / `odtis.org`.

`http://odtis.org` funcionará en minutos; HTTPS público requiere Cloudflare o cert en origen.

### DNS en propagación: curl no responde pero el sitio ya está live

Síntoma: `dig odtis.org +short @1.1.1.1` muestra IPs Cloudflare (`104.x` / `172.x`) y **200 OK**, pero en tu Mac:

```bash
dig odtis.org +short
# 192.64.119.26 ← parking Namecheap (MAL)

curl -sI https://odtis.org
# cuelga o SSL error - va al parking, no a Cloudflare
```

**Causa:** tu resolver local (Mac/router/ISP) aún tiene **caché DNS antigua** de Namecheap.

**Prueba bypass (confirma que el sitio funciona):**

```bash
curl -sI --resolve odtis.org:443:104.21.6.193 https://odtis.org | head -5
# HTTP/2 200
```

**Arreglo en Mac:**

1. **Preferencias → Red → Wi‑Fi → Detalles → DNS** → `+` añade:

- `1.1.1.1`
- `8.8.8.8`
- (opcional) quita otros DNS viejos

1. Aplicar y vaciar caché:

```bash
sudo dscacheutil -flushcache
sudo killall -HUP mDNSResponder
```

1. Cierra el navegador por completo; ventana privada → [https://odtis.org](https://odtis.org)
2. Comprueba:

```bash
dig odtis.org +short
# debe mostrar 104.x / 172.x, NO 192.64.119.26

curl -sI https://odtis.org | head -5
# HTTP/2 200
```

Si tras cambiar DNS en Mac sigue mal, reinicia el router o prueba con **datos móviles** (otra red). La propagación global puede tardar **hasta 24-48 h** en algunos ISPs; Cloudflare ya está bien configurado.

### Probar sin caché del navegador

- Ventana privada, o
- `https://odtis.org/?nocache=1`
- Cloudflare → **Caching → Purge Everything** tras el primer deploy

### Si el dominio es nuevo

La propagación de NS puede tardar **minutos a 48 h**. Mientras tanto `dig odtis.org` puede estar vacío aunque el servidor responda bien en localhost.

---

## Referencias


| Recurso          | Ruta                                 |
| ---------------- | ------------------------------------ |
| Build            | `odtis/scripts/build-site.sh`        |
| Deploy           | `odtis/scripts/deploy-ec2.sh`        |
| Nginx (Flexible) | `odtis/scripts/nginx-odtis.org.conf` |
| MkDocs           | `odtis/site/mkdocs.yml`              |


---

*Junio 2026 - EC2 + Cloudflare SSL **Flexible** · finnectos.com + odtis.org*