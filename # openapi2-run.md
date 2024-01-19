# openapi2-run.yaml
swagger: '2.0'
info:
  title: Vertex AI Chat API
  description: An API for interacting with a chat model on Vertex AI
  version: 1.0.0
schemes:
  - https
produces:
  - application/json
x-google-backend:
  address: https://summaryapi-image-nhz45gwa6a-et.a.run.app
security:
  - api_key: []
paths:
  /:
    get:
      summary: Render the index page
      responses:
        200:
          description: The index page
          content:
            text/html:
              schema:
                type: string
  /palm2:
    get:
      summary: Generate a chat response
      description: Generates a chat response based on a user-provided query
      parameters:
        - in: query
          name: user_input
          schema:
            type: string
          required: true
          description: The user's input query
      responses:
        200:
          description: A JSON object containing the chat response
          content:
            application/json:
              schema:
                type: object
                properties:
                  content:
                    type: string
                    description: The generated chat response
    post:
      summary: Generate a chat response (alternative method)
      description: Generates a chat response based on a user-provided query submitted as a form value
      requestBody:
        content:
          application/x-www-form-urlencoded:
            schema:
              type: object
              properties:
                user_input:
                  type: string
                  description: The user's input query
      responses:
        200:
          description: A JSON object containing the chat response
          content:
            application/json:
              schema:
                type: object
                properties:
                  content:
                    type: string
                    description: The generated chat response