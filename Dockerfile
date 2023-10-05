FROM python
COPY . /app/
WORKDIR /app
RUN pip3 install flake8 \
  && pip3 install pylint \
  && pip3 install python-dotenv \
  && pip3 install requests
