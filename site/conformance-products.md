---
title: Certified ODTIS products
description: Public registry of ODTIS self-certified and L3 certified products — live from the conformance registry API with offline fallback.
---

# Certified ODTIS products

<div class="odtis-hub-hero" markdown="1">

Public list of implementations that published an ODTIS conformance statement and opted into the registry.

<p class="odtis-hub-meta" markdown="1">
<strong>API:</strong> <a href="https://api.registry.odtis.org/v1/products">GET /v1/products</a> |
<strong>List your product:</strong> <a href="../conformance/certification/self-cert-guide.md">Self-certification guide</a> |
<strong>Badges:</strong> <a href="https://github.com/odtis/odtis-registry-api/blob/main/docs/BADGE-EMBED.md">Embed guide</a>
</p>

</div>

!!! info "Staging L2 vs L3 certified"
    **L2 self-certified** entries (sandbox or staging) reflect honest self-assessment with published evidence — they are **not** the same as **L3 certified** products that completed the [Certification program](../governance/CERTIFICATION.md) with an independent auditor.

    Label embeds and marketing copy accordingly: use L2 badges and say “self-certified (staging)” until an L3 audit is complete.

<div id="odtis-products-status" class="odtis-products-status" aria-live="polite"></div>

<div class="odtis-table-scroll">
<table id="odtis-products-table" class="odtis-products-table">
  <thead>
    <tr>
      <th scope="col" data-sort="name">Product</th>
      <th scope="col" data-sort="vendor">Vendor</th>
      <th scope="col" data-sort="level">Level</th>
      <th scope="col" data-sort="environment">Environment</th>
      <th scope="col" data-sort="profiles">Profiles</th>
      <th scope="col" data-sort="country">Country</th>
      <th scope="col" data-sort="verified_date">Verified</th>
      <th scope="col">Badge</th>
    </tr>
  </thead>
  <tbody id="odtis-products-body">
    <tr data-static-fallback="1">
      <td><a href="https://odtis.org/implementation/statements/venid-sandbox/">VenID RI Sandbox</a></td>
      <td>VenID</td>
      <td><span class="odtis-level odtis-level-l2">L2 self-certified</span></td>
      <td><span class="odtis-env odtis-env-sandbox">sandbox</span></td>
      <td>core-identity, trust-network</td>
      <td>VE</td>
      <td>2026-06-23</td>
      <td>
        <a href="https://api.registry.odtis.org/v1/badges/L2/core-identity.svg" title="ODTIS L2 Core Identity">
          <img src="https://api.registry.odtis.org/v1/badges/L2/core-identity.svg" alt="ODTIS L2 Core Identity" width="160" height="40" loading="lazy" />
        </a>
      </td>
    </tr>
  </tbody>
</table>
</div>

<noscript>
<p><em>JavaScript is disabled. Showing static fallback row only.</em></p>
</noscript>

<style>
.odtis-products-status {
  font-size: 0.875rem;
  color: var(--odtis-muted, #64748b);
  margin: 0.75rem 0 1rem;
}
.odtis-products-table th[data-sort] {
  cursor: pointer;
  user-select: none;
}
.odtis-products-table th[data-sort]:hover {
  color: var(--odtis-primary, #3949ab);
}
.odtis-level {
  display: inline-block;
  font-size: 0.78rem;
  font-weight: 600;
  padding: 0.15rem 0.45rem;
  border-radius: 0.25rem;
}
.odtis-level-l2 {
  background: var(--odtis-success-soft, rgba(46, 125, 50, 0.12));
  color: var(--odtis-success, #2e7d32);
}
.odtis-level-l3 {
  background: rgba(88, 28, 135, 0.12);
  color: #581c87;
}
.odtis-level-l1 {
  background: rgba(30, 58, 95, 0.12);
  color: #1e3a5f;
}
.odtis-env {
  font-size: 0.78rem;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  font-weight: 600;
}
.odtis-env-sandbox { color: #1565c0; }
.odtis-env-staging { color: #e65100; }
.odtis-env-production { color: #2e7d32; }
.odtis-products-empty td {
  text-align: center;
  font-style: italic;
  color: var(--odtis-muted, #64748b);
}
</style>

<script>
(function () {
  var STATIC_FALLBACK = [
    {
      id: "venid-sandbox",
      name: "VenID RI Sandbox",
      vendor: "VenID",
      level: "L2",
      environment: "sandbox",
      profiles: ["core-identity", "trust-network"],
      country: "VE",
      verified_date: "2026-06-23",
      statement_url: "https://odtis.org/implementation/statements/venid-sandbox/",
      badge_url: "https://api.registry.odtis.org/v1/badges/L2/core-identity.svg"
    }
  ];

  var BADGE_BASE = "https://api.registry.odtis.org";
  var sortKey = "name";
  var sortAsc = true;
  var products = [];

  function esc(text) {
    var d = document.createElement("div");
    d.textContent = text == null ? "" : String(text);
    return d.innerHTML;
  }

  function levelLabel(level) {
    if (level === "L3") return { text: "L3 certified", cls: "odtis-level-l3" };
    if (level === "L1") return { text: "L1 self-certified", cls: "odtis-level-l1" };
    return { text: "L2 self-certified", cls: "odtis-level-l2" };
  }

  function envClass(env) {
    if (env === "staging") return "odtis-env-staging";
    if (env === "production") return "odtis-env-production";
    return "odtis-env-sandbox";
  }

  function badgeUrl(product) {
    if (product.badge_url) return product.badge_url;
    var profile = (product.profiles && product.profiles[0]) || "core-identity";
    return BADGE_BASE + "/v1/badges/" + product.level + "/" + profile + ".svg";
  }

  function renderRow(product) {
    var lvl = levelLabel(product.level);
    var env = product.environment || "—";
    var profiles = Array.isArray(product.profiles) ? product.profiles.join(", ") : "—";
    var nameCell = product.statement_url
      ? '<a href="' + esc(product.statement_url) + '">' + esc(product.name) + "</a>"
      : esc(product.name);
    var bUrl = badgeUrl(product);
    return (
      "<tr>" +
      "<td>" + nameCell + "</td>" +
      "<td>" + esc(product.vendor) + "</td>" +
      '<td><span class="odtis-level ' + lvl.cls + '">' + esc(lvl.text) + "</span></td>" +
      '<td><span class="odtis-env ' + envClass(product.environment) + '">' + esc(env) + "</span></td>" +
      "<td>" + esc(profiles) + "</td>" +
      "<td>" + esc(product.country || "—") + "</td>" +
      "<td>" + esc(product.verified_date || "—") + "</td>" +
      '<td><a href="' + esc(bUrl) + '" title="ODTIS badge"><img src="' + esc(bUrl) + '" alt="ODTIS ' + esc(product.level) + ' badge" width="160" height="40" loading="lazy" /></a></td>' +
      "</tr>"
    );
  }

  function sortProducts(list) {
    return list.slice().sort(function (a, b) {
      var av = a[sortKey];
      var bv = b[sortKey];
      if (sortKey === "profiles") {
        av = (a.profiles || []).join(", ");
        bv = (b.profiles || []).join(", ");
      }
      av = av == null ? "" : String(av).toLowerCase();
      bv = bv == null ? "" : String(bv).toLowerCase();
      if (av < bv) return sortAsc ? -1 : 1;
      if (av > bv) return sortAsc ? 1 : -1;
      return 0;
    });
  }

  function renderTable(list) {
    var tbody = document.getElementById("odtis-products-body");
    if (!tbody) return;
    if (!list.length) {
      tbody.innerHTML = '<tr class="odtis-products-empty"><td colspan="8">No products listed yet. See the <a href="../conformance/certification/self-cert-guide.md">self-certification guide</a>.</td></tr>';
      return;
    }
    tbody.innerHTML = sortProducts(list).map(renderRow).join("");
  }

  function setStatus(msg) {
    var el = document.getElementById("odtis-products-status");
    if (el) el.textContent = msg;
  }

  function assetBase() {
    var path = window.location.pathname.replace(/\/$/, "");
    if (path.indexOf("/conformance/products") !== -1) {
      return "../../site/assets";
    }
    return "assets";
  }

  function loadConfig() {
    return fetch(assetBase() + "/registry-config.json", { cache: "no-cache" })
      .then(function (r) { return r.ok ? r.json() : { api_url: null }; })
      .catch(function () { return { api_url: null }; });
  }

  function loadFromApi(apiUrl) {
    return fetch(apiUrl.replace(/\/$/, "") + "/v1/products", { cache: "no-cache" })
      .then(function (r) {
        if (!r.ok) throw new Error("API " + r.status);
        return r.json();
      })
      .then(function (data) { return data.products || []; });
  }

  function loadStaticJson() {
    return fetch(assetBase() + "/products.json", { cache: "no-cache" })
      .then(function (r) {
        if (!r.ok) throw new Error("static JSON missing");
        return r.json();
      })
      .then(function (data) { return data.products || []; });
  }

  function initSort() {
    document.querySelectorAll("#odtis-products-table th[data-sort]").forEach(function (th) {
      th.addEventListener("click", function () {
        var key = th.getAttribute("data-sort");
        if (sortKey === key) {
          sortAsc = !sortAsc;
        } else {
          sortKey = key;
          sortAsc = true;
        }
        renderTable(products);
      });
    });
  }

  function boot() {
    initSort();
    loadConfig().then(function (cfg) {
      var apiUrl = cfg && cfg.api_url;
      if (apiUrl) {
        BADGE_BASE = apiUrl.replace(/\/$/, "");
        return loadFromApi(apiUrl)
          .then(function (list) {
            products = list.length ? list : STATIC_FALLBACK;
            setStatus("Live registry (" + apiUrl + ") · " + products.length + " product(s)");
          })
          .catch(function () {
            return loadStaticJson()
              .then(function (list) {
                products = list.length ? list : STATIC_FALLBACK;
                setStatus("Static snapshot (API unreachable) · " + products.length + " product(s)");
              })
              .catch(function () {
                products = STATIC_FALLBACK;
                setStatus("Static fallback · " + products.length + " product(s)");
              });
          });
      }
      return loadStaticJson()
        .then(function (list) {
          products = list.length ? list : STATIC_FALLBACK;
          setStatus("Static snapshot · " + products.length + " product(s)");
        })
        .catch(function () {
          products = STATIC_FALLBACK;
          setStatus("Static fallback · " + products.length + " product(s)");
        });
    }).then(function () {
      renderTable(products);
    });
  }

  if (typeof document$ !== "undefined" && document$.subscribe) {
    document$.subscribe(boot);
  } else if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else {
    boot();
  }
})();
</script>

---

## Submit your product

1. Complete [L1 and L2 self-assessment](../conformance/certification/self-cert-guide.md) with published evidence.
2. Open a PR to [`certified-products.yaml`](../conformance/certification/certified-products.yaml) — see [submission workflow](https://github.com/odtis/odtis-registry-api/blob/main/docs/SUBMISSION-WORKFLOW.md).
3. After merge, your entry appears here and at `GET /v1/products`.

For L3 production certification, see the [Certification program](../governance/CERTIFICATION.md) and [L3 audit checklist](../conformance/certification/L3-AUDIT-CHECKLIST.md).
