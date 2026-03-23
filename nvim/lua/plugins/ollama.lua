local cfg = require('config.ollama')

return {
  {
    'nomnivore/ollama.nvim',
    dependencies = {
      'nvim-lua/plenary.nvim',
    },

    cmd = { 'Ollama', 'OllamaModel', 'OllamaServe', 'OllamaServeStop' },

    keys = {
      {
        '<leader>oo',
        ":<c-u>lua require('ollama').prompt()<cr>",
        desc = 'ollama prompt',
        mode = { 'n', 'v' },
      },
      {
        '<leader>oe',
        ":<c-u>lua require('ollama').prompt('Explain_Code')<cr>",
        desc = 'ollama explain code',
        mode = { 'n', 'v' },
      },
      {
        '<leader>oi',
        ":<c-u>lua require('ollama').prompt('Improve_Code')<cr>",
        desc = 'ollama improve code',
        mode = { 'n', 'v' },
      },
      {
        '<leader>of',
        ":<c-u>lua require('ollama').prompt('Fix_Code')<cr>",
        desc = 'ollama fix code',
        mode = { 'n', 'v' },
      },
      {
        '<leader>ot',
        ":<c-u>lua require('ollama').prompt('Generate_Tests')<cr>",
        desc = 'ollama generate tests',
        mode = { 'n', 'v' },
      },
      {
        '<leader>om',
        '<cmd>OllamaModel<cr>',
        desc = 'ollama pick model',
      },
      {
        '<leader>os',
        '<cmd>OllamaServe<cr>',
        desc = 'ollama serve start',
      },
      {
        '<leader>ox',
        '<cmd>OllamaServeStop<cr>',
        desc = 'ollama serve stop',
      },
    },

    opts = {
      model = cfg.models.default,
      url = cfg.url,
      serve = cfg.serve,

      prompts = {
        Explain_Code = {
          prompt = 'Explain this $ftype code briefly and concretely:\n\n```$ftype\n$sel\n```',
          model = cfg.models.default,
          input_label = '> ',
          action = 'display',
        },

        Improve_Code = {
          prompt = 'Improve this $ftype code conservatively. Keep behavior unchanged.\nReturn only a single fenced code block in $ftype.\n\n```$ftype\n$sel\n```',
          model = cfg.models.default,
          input_label = '> ',
          action = 'display_replace',
          extract = '```$ftype\n(.-)```',
        },

        Fix_Code = {
          prompt = 'Fix likely bugs in this $ftype code. Keep the patch minimal.\nReturn only a single fenced code block in $ftype.\n\n```$ftype\n$sel\n```',
          model = cfg.models.fallback,
          input_label = '> ',
          action = 'display_replace',
          extract = '```$ftype\n(.-)```',
        },

        Generate_Tests = {
          prompt = 'Write focused tests for this $ftype code.\nReturn only a single fenced code block in $ftype.\n\n```$ftype\n$sel\n```',
          model = cfg.models.alt,
          input_label = '> ',
          action = 'display',
          extract = '```$ftype\n(.-)```',
        },
      },
    },
  },
}
