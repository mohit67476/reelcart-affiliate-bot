
# ReelCart Affiliate Link Bot (No Code Render Setup)

## 🚀 How to Use

1. Upload this folder to your GitHub account
2. Go to https://render.com → New Web Service → Connect GitHub → Select this repo
3. Set these environment variables:
   - EARNKARO_EMAIL
   - EARNKARO_PASSWORD
   - MEESHO_EMAIL
   - MEESHO_PASSWORD
4. Use POST /generate-affiliate with:
```json
{
  "platform": "meesho",
  "product_url": "https://meesho.com/sample-product"
}
```
5. Result: Affiliate link generated
