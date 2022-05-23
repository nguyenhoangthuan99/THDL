import axios from "axios";


const axiosClient = axios.create({
  baseURL: "http://localhost:8000/",
  headers: {
    "Content-Type": "application/json",
  },
});

const api = {

    async searchall(data) {
        const url = "/search";
        return axiosClient.post(url, data,
            {
              headers: { "X-Requested-With": "XMLHttpRequest" ,"Access-Control-Allow-Origin":"*"},
            });
      },
    async searchOneWeb(data,web){
        const url = `/search/${web}`;
        return axiosClient.post(
        url,
        data,
        {
            headers: { "X-Requested-With": "XMLHttpRequest" },
        }
        );
    },
    async  getResult(task){
        const url = `/result/${task}`;
        return axiosClient.get(url);
    }
}

export default api;