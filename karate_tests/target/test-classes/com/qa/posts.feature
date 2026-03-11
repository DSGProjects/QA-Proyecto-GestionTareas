Feature: Posts API Tests

Background:
* url 'http://127.0.0.1:8000'

Scenario: Crear post y get exitosamente
Given path '/posts'
And request { title: 'QA_API_Test_Create_Task_Valid', body: 'Smoke test for task creation endpoint', userId: 1 }
When method POST
Then status 200
And assert responseTime < 500
And match response.id == '#number'
And match response == {id: '#number', title: '#string', body: '#string', userId: '#number'}

* def post_id = response.id

Given path '/posts/'+ post_id
When method GET
Then status 200
And assert responseTime < 500
And match response.id == post_id
And match response.title == '#string' 


Scenario: POST + PUT valido

Given path '/posts'
And request { title: 'QA_API_Test_Create_Task_Valid', body: 'Smoke test for task creation endpoint', userId: 1 }
When method POST
Then status 200
And assert responseTime < 500
And match response.id == '#number'
And match response.title == '#string'
* def post_id = response.id

Given path '/posts/' +post_id
And request {title: 'Updated Title', body: 'Updated Body', userId: 99}
When method PUT
Then status 200
And assert responseTime < 500
And match response.id == '#number'
And match response.title == '#string'


Scenario: POST + DELETE + GET not found

Given path '/posts'
And request { title: 'QA_API_Test_Create_Task_Valid', body: 'Smoke test for task creation endpoint', userId: 1 }
When method POST
Then status 200
And assert responseTime < 500
And match response.id == '#number'
And match response.title == '#string'
* def post_id = response.id

Given path '/posts/' + post_id
When method DELETE
Then status 200
And match response.message == 'Post deleted'

Given path '/posts/' + post_id
When method GET
Then status 200
And assert responseTime < 500
And match response == {error: '#string'}
And match response.error == 'Post not found'

Scenario: GET post ID no existe

Given path '/posts/9999'
When method GET
Then status 200
And assert responseTime < 500
And match response == { error: '#string' }
And match response.error == 'Post not found'

Scenario: PUT not found

Given path '/posts/9999'
And request {title: 'Updated Title', body: 'Updated Body', userId: 99}
When method PUT
Then status 200
And match response == {error:'#string'}
And match response.error == 'Post not found'

Scenario: Listar todas las tareas

Given path '/posts'
And request {title:'QA-API_Test', body:'test', userId:1}
When method POST
Then status 200

Given path '/posts'
And request {}
When method GET
Then status 200
And assert responseTime < 500
And match response == '#array'
And match response[0].id == 1