local ls = require("luasnip")
local s = ls.snippet
local t = ls.text_node
local i = ls.insert_node

ls.add_snippets("tex", {
  -- Snippet for a definition
  s("def", {
    t("\\begin{definition}"),
    t("\\label{def:}"),
    t({"", "  "}), i(1, "Název definice"),
    t({"", "\\end{definition}"})
  }),
  -- Snippet for theorem
  s("thm", {
    t("\\begin{theorem}"),
    t("\\label{def:}"),
    t({"", "  "}), i(1, "Název věty"),
    t({"", "\\end{theorem}"})
  }),
})
