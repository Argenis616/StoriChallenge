<a name="readme-top"></a>
<!--
*** Thanks to Best-README-Template. for this templete :)
-->

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="https://upload.wikimedia.org/wikipedia/commons/b/b0/Stori_Logo_2023.svg" alt="Logo" width="150" height="150">
  </a>
  <h3 align="center">Stori Challege</h3>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#designe">Desinge</a></li>
      <ul>
        <li><a href="#resquest-flow">Request flow</a></li>
      </ul>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

This project is built on AWS, leveraging services such as S3, EKS, RDS, and LoadBalancer. It follows a microservices-oriented architecture and adheres to Clean Architecture principles, aiming to create a scalable system.

With a focus on flexibility and scalability, the project harnesses the power of AWS infrastructure to seamlessly integrate storage, containerization, and database services. The microservices architecture enhances modularity and maintainability, while Clean Architecture principles guide the organization of the codebase for clarity and extensibility.

We prioritize not only the functionality of the system but also the maintainability and adaptability to future changes. This project is a testament to our commitment to building robust, scalable solutions using industry-leading cloud services.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With
This project leverages a diverse set of modern technologies and tools to ensure efficiency and high-quality functionality. Here are some key technologies at play:

* [![Python][Python-badge]][Python-url]
* [![Gmail][Gmail-badge]][Gmail-url]
* [![AWS][AWS-badge]][AWS-url]
* [![RDS][RDS-badge]][RDS-url]
* [![S3][S3-badge]][S3-url]
* [![Kubernetes][Kubernetes-badge]][Kubernetes-url]
* [![Docker][Docker-badge]][Docker-url]
* [![MySQL][MySQL-badge]][MySQL-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.


<!-- USAGE EXAMPLES -->
## Usage

To use this service, we have exposed an endpoint on AWS. 
```sh
/create-user-summary/{filename}/{account} 
```
```txt
Where "filename" should be the filename without the .csv extension

And "account" should be an existing account in our DB.
```

Is will send the summary email to the email associated with the acount
```sh
For filename use test
```
If you want to use diferent file we should upload the file to the S3 bucket first 

Endpoint:
```sh
http://a3e09f24fe9284289abddadf695d0ced-1102330508.us-east-1.elb.amazonaws.com/create-user-summary/{filename}/{account}
```

Example :
```sh
http://a3e09f24fe9284289abddadf695d0ced-1102330508.us-east-1.elb.amazonaws.com/create-user-summary/test/839755
```

| User Account | email |
| -------- | -------- |
| 947368     | asce616@gmail.com     |
| 839755 | alfonso.medina@storicard.com |

With the account number 839755, the email will be sent to the recruiter Alfonso Medina at alfonso.medina@storicard.com. If you want the email to be sent to a specific address, please send a message to request adding it to the database for email delivery. Currently, this functionality is beyond the scope of the project.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Local usage

Before you begin, ensure you have the following prerequisites:

- An AWS account: You need an AWS account to generate the necessary configurations for S3, EKS, RDS, and IAM credentials with the required permissions.

- Software installations:
  - Python 3.8 or higher
  - Docker
  - Docker Compose

### Installation

#### Fast local installation

For fast local testing you can pull the dockerized application from a DockerHub account and just run it locally.

1. Use the DockerHub image:
   ```sh
   docker pull asce616/stori
   ```
2. Check the image status and note the image ID:
   ```sh
   docker images -a
   ```
3.  Run the Docker image:
   ```sh
   docker run -p 127.0.0.1:8080:8080 [IMAGE_ID]
   ```

4. Test as before but use these endpoint
Endpoint:
```sh
localhost:8080/create-user-summary/{filename}/{account}
```

#### Slow Local installation

Follow these steps to set up and run the application:

1. Clone the repository:
   ```sh
   git clone https://github.com/Argenis616/storyChallenge.git
   ```
2. Open and complete the information in the following files:
   ```sh
   vi ~/stori/app/common/config.py
   vi ~/stori/credentials
   ```
3. Build the Docker image:
   ```sh
   docker-compose up
   ```
4. Check the image status and note the image ID:
   ```sh
   docker images -a
   ```
5. Run the Docker image:
   ```sh
   docker run -p 127.0.0.1:8080:8080 [IMAGE_ID]
   ```
#### local installation (No docker)

1. Clone the repository:
   ```sh
   git clone https://github.com/Argenis616/storyChallenge.git
   ```
2. Open and complete the information in the following files:
   ```sh
   vi ~/stori/app/common/config.py
   vi ~/stori/credentials

3. Activate the virtual environment:
   ```sh
   source .venv/bin/activate
   ```
4. Install the required Python libraries:
   ```sh
   pip install -r requirements.txt
   ```
5. Start the service:
   ```sh
   uvicorn main:app --reload
   ```

Note: 

<p align="right">(<a href="#readme-top">back to top</a>)</p>






<!-- Desinge -->
## Architecture Design

<div align="center">
  <a>
    <img src="https://onedrive.live.com/embed?resid=C1439FE57082E86A%21136631&authkey=%21ADX7H3nMLKzQ2mo&width=831&height=971" width="400" height="500" />
  </a>

</div>

### Resquest flow

1. user send GET request to endpoint
2. ⁠Process file service gets the file from S3 bucket
3. ⁠Process file service searchs for user_id from Users table using the account
4. ⁠Service creates the list of transactions based on the .csv file
5. ⁠Process file service searchs for email from Users table using the account 
6. ⁠Services creates the data and metadate content of the summary email.
7. ⁠Process file service send request to Notification Service with a template_id, email_data_content and email_metadata
8. ⁠Notifications service sends email with the selected template_id, and email_data_content and email_metadata
9. ⁠Process file service saves the list of transactions on Transactions table if email is sent
10. ⁠Process file service returns list of transactions that were saved in the DB.
11. ⁠User gets response with list of transactions and a 200 OK
12. If account is not found or filename is not found service returns 404 NOT FOUND
13. If something is wrong with an external service (S3, RDS, Gmail) service returns 500 INTERNAL SERVER ERROR

<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- CONTACT -->
## Contact

Jorge Argenis - argenis616@ciencias.unam.mx

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Python-badge]: https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[Gmail-badge]: https://img.shields.io/badge/gmail-EA4335?style=for-the-badge&logo=gmail&logoColor=white
[Gmail-url]: https://mail.google.com/
[AWS-badge]: https://img.shields.io/badge/aws-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white
[AWS-url]: https://aws.amazon.com/
[RDS-badge]: https://img.shields.io/badge/rds-232F3E?style=for-the-badge&logo=amazonrds&logoColor=white
[RDS-url]: https://aws.amazon.com/rds/
[S3-badge]: https://img.shields.io/badge/s3-232F3E?style=for-the-badge&logo=amazons3&logoColor=white
[S3-url]: https://aws.amazon.com/s3/
[Kubernetes-badge]: https://img.shields.io/badge/kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white
[Kubernetes-url]: https://kubernetes.io/
[Docker-badge]: https://img.shields.io/badge/docker-2496ED?style=for-the-badge&logo=docker&logoColor=white
[Docker-url]: https://www.docker.com/
[MySQL-badge]: https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white
[MySQL-url]: https://www.mysql.com/