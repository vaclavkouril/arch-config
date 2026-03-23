-- Core UI & editing plugins

return {
  -- Theme
  {
    'navarasu/onedark.nvim',
    priority = 1000,
    config = function()
      require('onedark').load()
    end,
  },

  -- Statusline
  {
    'nvim-lualine/lualine.nvim',
    dependencies = { 'nvim-tree/nvim-web-devicons', lazy = true },
    opts = {
      options = {
        icons_enabled = false,
        theme = 'onedark',
        component_separators = '|',
        section_separators = '',
      },
    },
  },

  -- Indentation guides
  {
    'lukas-reineke/indent-blankline.nvim',
    main = 'ibl',
    opts = {},
  },

  -- Comments: gc, gcc, etc.
  {
    'numToStr/Comment.nvim',
    opts = {},
  },

  -- Which-key: discover keymaps
  {
    'folke/which-key.nvim',
    opts = {
      defaults = {
        ['<leader>d'] = { name = '+debug' },
      },
    },
  },

  -- Barbar tabline
  {
    'romgrk/barbar.nvim',
    dependencies = {
      'lewis6991/gitsigns.nvim',
      'nvim-tree/nvim-web-devicons',
    },
    init = function()
      vim.g.barbar_auto_setup = false
    end,
    opts = {},
    version = '^1.0.0',
  },

  -- Markdown / HTML preview with deno
  {
    'toppair/peek.nvim',
    event = { 'VeryLazy' },
    build = 'deno task --quiet build:fast',
    config = function()
      require('peek').setup()
      vim.api.nvim_create_user_command('PeekOpen', require('peek').open, {})
      vim.api.nvim_create_user_command('PeekClose', require('peek').close, {})
    end,
  },
}
