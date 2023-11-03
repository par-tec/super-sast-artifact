# FROM super-sast, copy-paste the Dockerfile is better?

FROM ghcr.io/par-tec/super-sast as super-sast

FROM python:3.11.1-alpine as base_python
COPY --from=super-sast / /
# RUN apt-get update
ADD main.py /
ADD entrypoint.sh /
ADD sast_to_log.py /

RUN mkdir parse_scripts
RUN mkdir log_dir
RUN ls -lah log_dir
ADD parse_scripts/bandit.py /parse_scripts
ADD request.py /

RUN chmod +x /entrypoint.sh
RUN chmod +x /sast_to_log.py
RUN chmod +x /parse_scripts/*
RUN chmod +x /main.py

ENTRYPOINT ["/entrypoint.sh"]