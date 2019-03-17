FROM "python"

COPY ./* /home/lapetite/

WORKDIR /home/lapetite

RUN ls /home/lapetite

RUN cd /home/lapetite && \
	pip install -r requirements.txt

ENTRYPOINT ["python","bot.py"]