# GeoMoose for Docker
FROM docker.io/debian:13
MAINTAINER Dan "Ducky" Little <@theduckylittle>

ENV LANG C.UTF-8
# RUN update-locale LANG=C.UTF-8

# Update and upgrade system
RUN find /etc/apt/sources.list* -type f -exec sed -i 's/Types: deb/Types: deb deb-src /' '{}' + && \
    apt-get -qq update --fix-missing && apt-get -qq --yes upgrade && \
    apt-get install -y apache2 git supervisor

# Install MapServer compilation prerequisites
RUN apt-get build-dep -y mapserver
RUN apt-get install -y libexempi-dev

# Install MapServer itself
RUN git clone --depth=1 --branch=branch-8-4 https://github.com/mapserver/mapserver /usr/local/src/mapserver

# Compile Mapserver for Apache
RUN mkdir /usr/local/src/mapserver/build && \
    cd /usr/local/src/mapserver/build && \
    cmake ../ -DWITH_THREAD_SAFETY=ON \
        -DUSE_PROJ=ON \
        -DWITH_KML=ON \
        -DWITH_SOS=ON \
        -DWITH_WMS=ON \
        -DWITH_FRIBIDI=ON \
        -DWITH_HARFBUZZ=ON \
        -DWITH_ICONV=ON \
        -DWITH_CAIRO=ON \
        -DWITH_RSVG=ON \
        -DWITH_MYSQL=ON \
        -DWITH_GEOS=ON \
        -DWITH_POSTGIS=ON \
        -DUSE_GDAL=ON \
        -DWITH_CURL=ON \
        -DWITH_CLIENT_WMS=ON \
        -DWITH_CLIENT_WFS=ON \
        -DWITH_WFS=ON \
        -DWITH_WCS=ON \
        -DWITH_LIBXML2=ON \
        -DWITH_GIF=ON \
        -DWITH_EXEMPI=ON \
        -DWITH_XMLMAPFILE=ON \
    -DWITH_FCGI=0 && \
    make && \
    make install && \
    ldconfig

# Link to cgi-bin executable
RUN chmod o+x /usr/local/bin/mapserv
RUN ln -s /usr/local/bin/mapserv /usr/lib/cgi-bin/mapserv
RUN chmod 755 /usr/lib/cgi-bin
COPY etc/mapserver.conf /usr/local/etc/mapserver.conf


# Configure localhost in Apache
RUN a2enmod actions cgi alias headers
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf
RUN echo "ErrorLog /dev/stdout" >> /etc/apache2/apache2.conf
COPY etc/000-default.conf /etc/apache2/sites-available/

# Configure supervisor
RUN mkdir -p /var/log/supervisor
COPY etc/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Install TinyOWS

## First install postgresql and postgis

# RUN apt-get install -y autoconf build-essential cmake docbook-mathml docbook-xsl libboost-dev libboost-filesystem-dev libboost-timer-dev libcgal-dev libcunit1-dev libgdal-dev libgeos++-dev libgeotiff-dev libgmp-dev libjson0-dev libjson-c-dev liblas-dev libmpfr-dev libopenscenegraph-dev libpq-dev libproj-dev libxml2-dev postgresql xsltproc wget flex libfcgi-dev postgis postgresql-9.3-postgis-2.1


# Compile TinyOWS
# RUN git clone https://github.com/mapserver/tinyows.git
# RUN cd tinyows && autoconf && ./configure && make && make install && cp tinyows /usr/lib/cgi-bin/tinyows
# get rid of tinyows leftovers
# RUN rm -rf tinyows
#--with-shp2pgsql=/usr/lib/postgresql/9.5/bin/shp2pgsql

# COPY etc/tinyows.xml /etc/tinyows.xml

# End of TinyOWS Install

# Get the database going

# create a landing place for the places data
# RUN mkdir -p /data/places
# RUN chmod a+rx /data
# RUN chmod a+rwx /data/places
# COPY data/places/* /data/places/

# now create a database and load the data into it.
# COPY createdb.sh /tmp
# RUN chmod +x /tmp/createdb.sh
# RUN service postgresql start ; su - postgres -c "/tmp/createdb.sh"

## Install the GeoMoose demo data

# create a new directory
# RUN mkdir -p /data

# clone the data repo into a useful directory.
RUN git clone --depth=1 https://github.com/geomoose/gm3-demo-data.git /data
RUN chown www-data:www-data -R /data

# Restart Apache
RUN service apache2 restart

EXPOSE 80

ENV HOST_IP `ifconfig | grep inet | grep Mask:255.255.255.0 | cut -d ' ' -f 12 | cut -d ':' -f 2`


CMD ["/usr/bin/supervisord"]
