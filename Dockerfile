FROM debian:bullseye-slim as deployment
# system dependencies
RUN apt-get update
RUN apt-get install -y python3 python3-pip

# variables
ENV PROJDIR=/app
ENV VIRTUAL_ENV=/virtualenv

# folder setup
RUN pip3 install virtualenv
RUN python3 -m virtualenv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/env/bin:$PATH"
COPY funny_app.py requirements.txt $PROJDIR/
WORKDIR $PROJDIR/

# install
RUN pip3 install -r requirements.txt
USER www-data
EXPOSE 8001
CMD ["python3", "funny_app.py"]

