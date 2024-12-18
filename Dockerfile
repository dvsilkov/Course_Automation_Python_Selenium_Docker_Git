FROM python
WORKDIR /Automation_project/

# Copy the dependencies file to the working directory
COPY ./requirements.txt .

# Install Python dependencies
RUN pip3 install -r requirements.txt

RUN apt update
RUN apt install -y wget

# Install chrome browser
RUN apt update
RUN apt list --upgradeable
RUN wget --no-check-certificate https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN dpkg -i google-chrome-stable_current_amd64.deb ; apt -y --fix-broken install
RUN dpkg -i google-chrome-stable_current_amd64.deb

# Install chrome driver
RUN apt install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# Install Allure
RUN apt install -y default-jre
RUN wget --no-check-certificate https://github.com/allure-framework/allure2/releases/download/2.18.1/allure_2.18.1-1_all.deb
RUN dpkg -i allure_2.18.1-1_all.deb

# Команда для сборки образа: docker build . -t pytest_selenium_runner