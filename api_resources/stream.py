from sanic import response


async def stream(request):
    async def streaming_response(response):
        """
            Here I could iterate over a generator so I don't need to
            save the file in my hard disk
        """

        def range_file():
            # Watch out for this number (range number)! You don't want to crash you computer.
            # Once the file is fully streamed,
            # it will load itself fully on your browser (ALL THE FILE ON THE MEMORY OF YOUR COMPUTER)
            # So... again.. Watch out!
            # I don't want to say: "I told you so..."
            for i in range(1, 1000000):
                yield "Line {}\n".format(str(i))

        for line in range_file():
            response.write(line)

    headers = {"Content-Disposition": "attachment; filename = big_file.txt"}
    return response.stream(streaming_response, headers=headers)


async def stream_from_file(request):
    """
        Stream from file on your hard disk
    """
    headers = {"Content-Disposition": "attachment; filename = big_file.txt"}
    return await response.file_stream("./static/big_file.txt", headers=headers)
