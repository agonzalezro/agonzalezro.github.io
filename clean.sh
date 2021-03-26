files=$(find static|sed "s/static\///g")

for file in $files; do
    ack "$file" > /dev/null
    if [ $? -eq 1 ]; then
        echo $file
    fi
done