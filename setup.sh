mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"yan.cunha2198@gmaill.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = true\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/config.toml