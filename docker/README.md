You need to choose, there is a red pill:

    npm install -g reveal-md
    reveal-md --theme=simple docker.md

Or you can choose the blue pill:

    docker build -t agonzalezro/reveal-md .
    docker run -d -v `pwd`:/slides -p 1948:1948 agonzalezro/reveal-md
    open `boot2docker ip`:1948/docker.md

Also, you can create a pdf file:

    reveal-md --theme=simple -r docker.pdf docker.md

or using the previously mentioned docker image :)
