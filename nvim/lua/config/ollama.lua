return {
  url = 'http://127.0.0.1:11434',

  models = {
    default = 'qwen2.5-coder:1.5b',
    fallback = 'qwen2.5-coder:0.5b',
    alt = 'codegemma:2b',
    heavy = 'qwen2.5-coder:3b',
  },

  serve = {
    on_start = false,
    command = 'ollama',
    args = { 'serve' },
    stop_command = 'pkill',
    stop_args = { '-SIGTERM', 'ollama' },
  },
}
