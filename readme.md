****<h1 align="center" style="font-weight: bold;">Python Back-end 💻</h1>

<p align="center">
 <a href="#tech">Technologies</a> • 
 <a href="#started">Getting Started</a> • 
  <a href="#routes">API Endpoints</a> 
  <a href="#swagger">Swagger</a> •
 <!-- <a href="#colab">Collaborators</a> •
 <a href="#contribute">Contribute</a> -->
</p>

<p align="center">
    <b>Simple description of what your project do or how to use it.</b>
</p>
<h2 id="tech">💻 Technologies</h2>

- list of all technologies you used
- Python
- Flask
- Sql

<h2 id="started">🚀 Getting started</h2>

Here you describe how to run your project locally

<h3>Prerequisites</h3>

Here you list all prerequisites necessary for running your project. For example:

- [Python](https://www.python.org)
- [Flask](https://github.com)
- [MySql](https://www.mysql.com)

<h3>Cloning</h3>

How to clone your project


```bash
git clone git@github.com:rcrossa/pythonbackend.git
```

<h3>Starting</h3>

How to start your project

```bash
- cd project-name
- python3 -m venv venv
- source venv/bin/activate 
```
<h4> In virtual enviroment run the following commands:</h4>

```bash
- pip install flask
- pip3 install flask_swagger_ui
- pip install mysql-conector-python
- pip install python-dotenv
- pip install flask-cors
- python3 index.py
```


 <h2 id="routes">📍 API Endpoints</h2>

The following endpoints are available:
​
| route               | description                                          
|----------------------|-----------------------------------------------------
| <kbd>GET /</kbd>     | retrieve a text example [response details](#get-text)
| <kbd>GET /api/movies</kbd>     | retrieve an object [response details](#get-object)
| <kbd>GET /api/movies/{id}</kbd>     | retrieve an object [response details](#get-movieby-id)
| <kbd>POST /api/movies/</kbd>     | retrieve a response [response details](#create-movie)
| <kbd>PUT /api/movies/{id}</kbd>     | retrieve a response [response details](#get-movie)
| <kbd>DELETE /api/movies/{id}</kbd>     | retrieve a response [response details](#delete-movie)


<h3 id="get-text">GET /</h3>

**RESPONSE**
```html
<h1>Hola mundo con flask 🐍</h1>
```
<h3 id="get-object">GET /api/movies</h3>

**RESPONSE**
```json
[
    {
        "banner": "1",
        "director": "teste",
        "id_movie": 1,
        "rating": "3",
        "release_date": "Fri, 22 Mar 2222 00:00:00 GMT",
        "title": "teste"
    }
]
```
<h3 id="get-movieby-id">GET /api/movies/{id}</h3>

**RESPONSE**
```json
{
    "banner": "1",
    "director": "teste",
    "id_movie": 1,
    "rating": [
        3
    ],
    "release_date": "Fri, 22 Mar 2222 00:00:00 GMT",
    "title": "teste"
}
```
<h3 id="create-movie">POST /api/movies/</h3>

**RESPONSE**
```json
{
    "response": "Movie created successfully"
}
```
<h3 id="update-movie">PUT /api/movies/{id}</h3>

**RESPONSE**
```json
{
    "banner": "1",
    "director": "teste",
    "id_movie": 1,
    "rating": [
        3
    ],
    "release_date": "Fri, 22 Mar 2222 00:00:00 GMT",
    "title": "teste"
}
```
<h3 id="delete-movie">DELETE /api/movies/{id}</h3>

**RESPONSE**
```json
{
  "response": "Movie deleted successfully"
}
```

<h3 id="swagger">Swagger</h3>
<h4>You can see information related to swagger in the path: /swagger</h4>


<!--<h3 id="post-auth-detail">POST /authenticate</h3>

**REQUEST**
```json
{
  "username": "fernandakipper",
  "password": "4444444"
}
``` -->

<!-- **RESPONSE**
```json
{
  "token": "OwoMRHsaQwyAgVoc3OXmL1JhMVUYXGGBbCTK0GBgiYitwQwjf0gVoBmkbuyy0pSi"
}

<h2 id="colab">🤝 Collaborators</h2>

Special thank you for all people that contributed for this project.

<table>
  <tr>
    <td align="center">
      <a href="#">
        <img src="https://avatars.githubusercontent.com/u/61896274?v=4" width="100px;" alt="Fernanda Kipper Profile Picture"/><br>
        <sub>
          <b>Fernanda Kipper</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="#">
        <img src="https://t.ctcdn.com.br/n7eZ74KAcU3iYwnQ89-ul9txVxc=/400x400/smart/filters:format(webp)/i490769.jpeg" width="100px;" alt="Elon Musk Picture"/><br>
        <sub>
          <b>Elon Musk</b>
        </sub>
      </a>
    </td>
    <td align="center">
      <a href="#">
        <img src="https://miro.medium.com/max/360/0*1SkS3mSorArvY9kS.jpg" width="100px;" alt="Foto do Steve Jobs"/><br>
        <sub>
          <b>Steve Jobs</b>
        </sub>
      </a>
    </td>
  </tr>
</table>

<h2 id="contribute">📫 Contribute</h2>

Here you will explain how other developers can contribute to your project. For example, explaining how can create their branches, which patterns to follow and how to open an pull request

1. `git clone https://github.com/Fernanda-Kipper/text-editor.git`
2. `git checkout -b feature/NAME`
3. Follow commit patterns
4. Open a Pull Request explaining the problem solved or feature made, if exists, append screenshot of visual modifications and wait for the review!

<h3>Documentations that might help</h3>

[📝 How to create a Pull Request](https://www.atlassian.com/br/git/tutorials/making-a-pull-request)

[💾 Commit pattern](https://gist.github.com/joshbuchea/6f47e86d2510bce28f8e7f42ae84c716) -->