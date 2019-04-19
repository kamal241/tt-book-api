# book-api
Adeva Technical Test - Book - api



## Setup & Installtion

- [Install virtual environment](https://github.com/kamal241/tt-book-api/new/master?readme=1#install-virtual-environment)
- [Clone repository](https://github.com/kamal241/tt-book-api/new/master?readme=1#clone-repository)
- [Go to directory](https://github.com/kamal241/tt-book-api/new/master?readme=1#go-to-the-directory)
- [Create virtual environment](https://github.com/kamal241/tt-book-api/new/master?readme=1#create-virtual-environment)
- [Activate Virtual environment](https://github.com/kamal241/tt-book-api/new/master?readme=1#activate-virtual-environment)
- [Install required libraries](https://github.com/kamal241/tt-book-api/new/master?readme=1#install-required-libraries)
- [Run Database migration](https://github.com/kamal241/tt-book-api/new/master?readme=1#run-database-migration)
- [Run the book-api](https://github.com/kamal241/tt-book-api/new/master?readme=1#run-the-book-api)

### Install virtual environment

  ```
  pip install virtualenv
  ```
  
### Clone repository

  ```
  git clone https://github.com/kamal241/tt-book-api.git
  ```
  
### Go to the directory

  ```
  cd tt-book-api/
  ```
  
### Create virtual environment

  ```
  virtualenv adeva-ex
  ```
### Activate virtual environment

  ```
  source adeva-ex/bin/activate
  ```

### Install required libraries

  ```
  pip install -r requirements.txt
  ```
  

### Run Database migration

  ```
  python migrate.py db init 
  python migrate.py db migrate
  python migrate.py db upgrade
  ```

### Run the book-api
  ```
  python run.py
  ```

## Testing

### Get the Postman Chrome extension from here
[Postman](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop?utm_source=chrome-app-launcher-info-dialog)

### Launch & Import adeva.postman_collection.json to POSTMAN
On the top bar Click on Import -> Import File (Choose the adeva.postman_collection.json ) -> Choose Files -> Open

### Test all the requirements

- GET    /api/external-books?name=A Clash of Kings
- GET    /api/v1/books
- GET    /api/v1/books/:id
- POST   /api/v1/books
- PATCH  /api/v1/books/:id
- DELETE /api/v1/books/:id
- GET    /api/v1/books?name=A Clash of Kings
- GET    /api/v1/books?release_date=2019


