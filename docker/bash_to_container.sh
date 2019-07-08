if [[ -n "$1" ]]; then
    result=$(docker ps | grep $1)
    if [[ -n "$result" ]]; then
        echo "Container exists. Connecting via bash.."
        sudo docker exec -it $1 bash 
    else
        echo "Container doesn't exist!"
    fi
else
    echo "First parm not given. You must provide CONTAINER_ID as 1st parm!"
    echo "See command: docker ps"
fi