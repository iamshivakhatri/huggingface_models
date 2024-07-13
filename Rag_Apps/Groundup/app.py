curl http://localhost:11434/api/generate -d '{ 
"model": "phi3",
"prompt": "How was world formed?",
"stream": false
}' | jq .
