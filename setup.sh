mkdir -p ~/.streamlit/

echo "\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
Headless = true\n\
\n\
" > ~/.streamlit/config.toml