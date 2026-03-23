-- Prolog language configuration

local ok, lspconfig = pcall(require, 'lspconfig')
if not ok then
  return
end

-- Ensure our custom prolog_lsp definition is loaded
pcall(require, 'lspconfig.prolog_lsp')

-- Attach Prolog LSP if available
if lspconfig.prolog_lsp then
  lspconfig.prolog_lsp.setup({})
end
