# Deployment Guide for Snakeskin Landing Page

Your landing page is a static site (HTML + CSS + JS) that can be deployed anywhere. Here are the easiest options:

---

## 🚀 Quick Deploy Options

### **1. Netlify Drop (Easiest - No Account Needed)**

**Steps:**
1. Go to [https://app.netlify.com/drop](https://app.netlify.com/drop)
2. Drag and drop your `dist` folder onto the page
3. Your site is live! You'll get a URL like `https://random-name.netlify.app`

**Pros:** Instant, no CLI, no config needed
**Cons:** Random URL (can upgrade to custom domain)

---

### **2. Netlify CLI (Recommended)**

**Install Netlify CLI:**
```bash
npm install -g netlify-cli
# or
brew install netlify-cli
```

**Deploy:**
```bash
cd /Users/opensource/Desktop/testing/my-landing-page
netlify deploy --dir=dist --prod
```

**First time setup:**
- You'll be asked to login (creates account if needed)
- Choose "Create & configure a new site"
- Follow prompts

**Pros:** Custom domain support, continuous deployment, free SSL
**Cons:** Requires CLI installation

---

### **3. Vercel**

**Install Vercel CLI:**
```bash
npm install -g vercel
```

**Deploy:**
```bash
cd /Users/opensource/Desktop/testing/my-landing-page
vercel --prod
```

**First time:**
- Login when prompted
- Accept defaults or customize

**Pros:** Fast CDN, great performance, free SSL
**Cons:** Requires CLI installation

---

### **4. GitHub Pages**

**Steps:**
1. Create a GitHub repository
2. Push your code:
```bash
cd /Users/opensource/Desktop/testing/my-landing-page
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

3. Go to repository Settings → Pages
4. Set source to `main` branch and `/dist` folder
5. Your site will be at `https://YOUR_USERNAME.github.io/YOUR_REPO`

**Pros:** Free, integrated with Git, custom domains
**Cons:** Requires Git setup

---

### **5. Surge.sh (Super Simple)**

**Install:**
```bash
npm install -g surge
```

**Deploy:**
```bash
cd /Users/opensource/Desktop/testing/my-landing-page/dist
surge
```

**First time:**
- Enter email and password to create account
- Choose a domain name (e.g., `my-snakeskin-site.surge.sh`)

**Pros:** Extremely simple, instant deployment
**Cons:** Basic features only

---

## 📝 Pre-Deployment Checklist

Before deploying, make sure:

- ✅ Run `python3 main.py` to build the latest version
- ✅ Check that `dist/index.html` exists and looks correct
- ✅ Test locally by opening `dist/index.html` in browser
- ✅ All images and assets are loading properly

---

## 🔄 Continuous Deployment

For automatic deployments when you make changes:

### **Netlify with Git:**
1. Push your code to GitHub/GitLab/Bitbucket
2. Connect repository in Netlify dashboard
3. Set build command: `python3 main.py`
4. Set publish directory: `dist`
5. Every push automatically deploys!

### **Vercel with Git:**
1. Push your code to GitHub/GitLab/Bitbucket
2. Import project in Vercel dashboard
3. Set build command: `python3 main.py`
4. Set output directory: `dist`
5. Auto-deploys on every push!

---

## 🌐 Custom Domain

All platforms support custom domains:

1. **Buy a domain** (Namecheap, Google Domains, etc.)
2. **Add to platform:**
   - Netlify: Domains → Add custom domain
   - Vercel: Settings → Domains
   - GitHub Pages: Settings → Pages → Custom domain
3. **Update DNS:**
   - Add CNAME record pointing to platform's URL
   - Or use platform's nameservers

---

## 💡 Recommended: Netlify Drop for Testing

**For your first deployment, I recommend:**

1. Open [https://app.netlify.com/drop](https://app.netlify.com/drop)
2. Drag your `dist` folder
3. Get instant live URL to share!

Then, if you like it, set up CLI for easier updates.

---

## 🆘 Need Help?

If you encounter issues:
- Make sure `dist/index.html` exists
- Check that all paths are relative (not absolute)
- Ensure Tailwind CDN and Lucide CDN are loading
- Test locally first before deploying
