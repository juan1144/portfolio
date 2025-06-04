/* CUSTOM TOOLTIPS JS */
document.addEventListener("DOMContentLoaded", () => {
  const OFFSET = 8;

  document.querySelectorAll(".tooltip-target").forEach(el => {
    const message = el.getAttribute("data-tooltip");
    const placement = el.getAttribute("data-placement") || "top";
    if (!message) return;

    const tooltip = document.createElement("div");
    tooltip.className = "tooltip-text";
    tooltip.textContent = message;
    tooltip.setAttribute("data-placement", placement);
    document.body.appendChild(tooltip);

    const showTooltip = () => {
      const rect = el.getBoundingClientRect();
      const ttRect = tooltip.getBoundingClientRect();

      let top = 0, left = 0;
      switch (placement) {
        case "top":
          top = rect.top - ttRect.height - OFFSET;
          left = rect.left + (rect.width - ttRect.width) / 2;
          break;
        case "bottom":
          top = rect.bottom + OFFSET;
          left = rect.left + (rect.width - ttRect.width) / 2;
          break;
        case "left":
          top = rect.top + (rect.height - ttRect.height) / 2;
          left = rect.left - ttRect.width - OFFSET;
          break;
        case "right":
          top = rect.top + (rect.height - ttRect.height) / 2;
          left = rect.right + OFFSET;
          break;
      }

      tooltip.style.top = `${top + window.scrollY}px`;
      tooltip.style.left = `${left + window.scrollX}px`;

      tooltip.classList.add("tooltip-visible");
    };

    const hideTooltip = () => {
      tooltip.classList.remove("tooltip-visible");
    };

    el.addEventListener("mouseenter", showTooltip);
    el.addEventListener("mouseleave", hideTooltip);
    el.addEventListener("focus", showTooltip);
    el.addEventListener("blur", hideTooltip);
  });
});
