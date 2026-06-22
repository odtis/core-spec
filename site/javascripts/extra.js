/* ODTIS spec site - Mermaid theme + palette sync */

(function () {
  function palette() {
    return document.body.getAttribute("data-md-color-scheme") === "slate"
      ? "dark"
      : "default";
  }

  function applyMermaidTheme() {
    if (typeof mermaid === "undefined") {
      return;
    }
    mermaid.initialize({
      startOnLoad: true,
      securityLevel: "loose",
      flowchart: {
        curve: "basis",
        padding: 14,
        htmlLabels: true,
        nodeSpacing: 42,
        rankSpacing: 48,
      },
      sequence: {
        diagramMarginX: 12,
        diagramMarginY: 8,
        actorMargin: 48,
        messageMargin: 32,
      },
      theme: palette(),
      themeVariables:
        palette() === "dark"
          ? {
              primaryColor: "#3949ab",
              primaryTextColor: "#e8eaf6",
              primaryBorderColor: "#7986cb",
              lineColor: "#9fa8da",
              secondaryColor: "#283593",
              tertiaryColor: "#1a237e",
            }
          : {
              primaryColor: "#e8eaf6",
              primaryTextColor: "#283593",
              primaryBorderColor: "#3949ab",
              lineColor: "#5c6bc0",
              secondaryColor: "#c5cae9",
              tertiaryColor: "#f5f7ff",
            },
    });
  }

  document$.subscribe(applyMermaidTheme);

  function wrapScrollTables(root) {
    var scope = root || document;
    scope.querySelectorAll(".md-typeset table").forEach(function (table) {
      if (table.closest(".odtis-spec-meta, .odtis-table-scroll")) {
        return;
      }
      var wrap = document.createElement("div");
      wrap.className = "odtis-table-scroll";
      table.parentNode.insertBefore(wrap, table);
      wrap.appendChild(table);
    });
  }

  document$.subscribe(function () {
    wrapScrollTables(document);
  });

  var observer = new MutationObserver(function () {
    applyMermaidTheme();
  });
  observer.observe(document.body, {
    attributes: true,
    attributeFilter: ["data-md-color-scheme"],
  });
})();
