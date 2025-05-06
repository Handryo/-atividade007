#!/bin/bash

OUTPUT="resultados.txt"
echo "=== Resultados da Atividade 007 ===" > "$OUTPUT"
echo "" >> "$OUTPUT"

for i in {01..10}; do
    SCRIPT="at007_questao${i}.py"
    echo ">>> python3 $SCRIPT" >> "$OUTPUT"
    python3 "$SCRIPT" >> "$OUTPUT" 2>&1
    echo "" >> "$OUTPUT"
    echo "-----------------------------" >> "$OUTPUT"
    echo "" >> "$OUTPUT"
done

echo "Todos os resultados foram salvos em $OUTPUT"
