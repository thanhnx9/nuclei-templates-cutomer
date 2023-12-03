# Spring RCE

This repository provide vulnerable applications to CVE-2022-22963 and CVE-2022-22965.

Also, You can find nuclei templates to check vulnerabilities.

CVE-2022-22965 vulnerable application original repository: [Spring4Shell-POC](https://github.com/reznok/Spring4Shell-POC)

## Download Repository

```
git clone https://github.com/justmumu/SpringShell.git
```

## Steps For CVE-2022-22965

```
$ cd <repository_directory>/CVE-2022-22965
$ docker-compose up
$ ## Wait for the application to run
$ nuclei -t <repository_directory>/nuclei-templates/CVE-2022-22965.yaml -u http://localhost:8080/helloworld/greeting
```

## Steps For CVE-2022-22963
```
$ cd <repository_directory>/CVE-2022-22963
$ docker-compose up
$ ## Wait for the application to run
$ nuclei -t <repository_directory>/nuclei-templates/CVE-2022-22963.yaml -u http://localhost:8080/
```