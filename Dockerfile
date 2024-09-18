FROM node:16
WORKDIR /root/Hyper_Speed0
COPY package*.json ./
RUN npm install
COPY . .
CMD ["node", "main.js"]
