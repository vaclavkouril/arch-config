-- Keymaps

local map = vim.keymap.set

-- Make space do nothing (leader handled by mapleader)
map({ 'n', 'v' }, '<Space>', '<Nop>', { silent = true })

-- Better up/down with wrapped lines
map('n', 'k', "v:count == 0 ? 'gk' : 'k'", { expr = true, silent = true })
map('n', 'j', "v:count == 0 ? 'gj' : 'j'", { expr = true, silent = true })

-- Diagnostics
map('n', '[d', vim.diagnostic.goto_prev, { desc = 'Go to previous diagnostic message' })
map('n', ']d', vim.diagnostic.goto_next, { desc = 'Go to next diagnostic message' })
map('n', '<leader>e', vim.diagnostic.open_float, { desc = 'Open floating diagnostic message' })
map('n', '<leader>q', vim.diagnostic.setloclist, { desc = 'Open diagnostics list' })

-- Telescope keymaps (lazy-loaded via builtin requires)
local tb = function() return require('telescope.builtin') end

map('n', '<leader>?', function() tb().oldfiles() end, { desc = '[?] Find recently opened files' })
map('n', '<leader><space>', function() tb().buffers() end, { desc = '[ ] Find existing buffers' })
map('n', '<leader>/', function()
  require('telescope.builtin').current_buffer_fuzzy_find(
    require('telescope.themes').get_dropdown {
      winblend = 10,
      previewer = false,
    }
  )
end, { desc = '[/] Fuzzily search in current buffer' })
map('n', '<leader>gf', function() tb().git_files() end, { desc = 'Search [G]it [F]iles' })
map('n', '<leader>sf', function() tb().find_files() end, { desc = '[S]earch [F]iles' })
map('n', '<leader>sh', function() tb().help_tags() end, { desc = '[S]earch [H]elp' })
map('n', '<leader>sw', function() tb().grep_string() end, { desc = '[S]earch current [W]ord' })
map('n', '<leader>sg', function() tb().live_grep() end, { desc = '[S]earch by [G]rep' })
map('n', '<leader>sd', function() tb().diagnostics() end, { desc = '[S]earch [D]iagnostics' })
map('n', '<leader>sr', function() tb().resume() end, { desc = '[S]earch [R]esume' })

-- Barbar keymaps
local nmap = vim.api.nvim_set_keymap
local opts = { noremap = true, silent = true }

-- Move to previous/next
nmap('n', '<A-,>', '<Cmd>BufferPrevious<CR>', opts)
nmap('n', '<A-.>', '<Cmd>BufferNext<CR>', opts)

-- Re-order to previous/next
nmap('n', '<A-<>', '<Cmd>BufferMovePrevious<CR>', opts)
nmap('n', '<A->>', '<Cmd>BufferMoveNext<CR>', opts)

-- Goto buffer in position...
for i = 1, 9 do
  nmap('n', '<A-' .. i .. '>', '<Cmd>BufferGoto ' .. i .. '<CR>', opts)
end
nmap('n', '<A-0>', '<Cmd>BufferLast<CR>', opts)

-- Pin/unpin buffer
nmap('n', '<A-p>', '<Cmd>BufferPin<CR>', opts)

-- Close buffer
nmap('n', '<A-c>', '<Cmd>BufferClose<CR>', opts)

-- New tab
nmap('n', '<A-=>', '<Cmd>tabnew<CR>', opts)

-- Magic buffer-picking mode
nmap('n', '<C-p>', '<Cmd>BufferPick<CR>', opts)

-- Buffer sorting
nmap('n', '<Space>bb', '<Cmd>BufferOrderByBufferNumber<CR>', opts)
nmap('n', '<Space>bd', '<Cmd>BufferOrderByDirectory<CR>', opts)
nmap('n', '<Space>bl', '<Cmd>BufferOrderByLanguage<CR>', opts)
nmap('n', '<Space>bw', '<Cmd>BufferOrderByWindowNumber<CR>', opts)
