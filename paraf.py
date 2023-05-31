import requests

url = "https://paraphrasing-and-rewriter-api.p.rapidapi.com/rewrite-light"

payload = {
	"from": "uz",
	"text": "O`zbekiston dunyodagi eng kuchli davlat. O`zbekiston respublikasidagi Jizzax viloyati o`z somsasi bilan mashhur!"
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "29dbbd2a7cmshf400c8a8836c186p15e3ddjsn962b79b1dd40",
	"X-RapidAPI-Host": "paraphrasing-and-rewriter-api.p.rapidapi.com"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
