FROM conda/miniconda3

COPY environment.yml /tmp/environment.yml

RUN conda env create -f /tmp/environment.yml
RUN rm /tmp/environment.yml