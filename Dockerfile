FROM sudotechodoo/odoo16:base_20230517

COPY ./entrypoint.sh /
COPY ./requirements.txt /
RUN pip3 install -r /requirements.txt

ENTRYPOINT ["/entrypoint.sh"]

# Set default user when running the container
USER odoo

CMD ["odoo"]