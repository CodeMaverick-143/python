# 🐍 Snakeskin Landing Page

A modern, beautiful landing page built with [Snakeskin](https://github.com/xplnhub/snakeskin) - a venomously fast Python web framework. Features a responsive design with Tailwind CSS, smooth animations, and Lucide icons.

![Snakeskin Landing Page](https://via.placeholder.com/1200x600/4F46E5/FFFFFF?text=Snakeskin+Landing+Page)

## ✨ Features

- **🎨 Modern Design**: Beautiful gradient backgrounds, glass morphism effects, and smooth animations
- **📱 Fully Responsive**: Looks great on all devices - mobile, tablet, and desktop
- **⚡ Lightning Fast**: Static HTML generation for optimal performance
- **🎯 Component-Based**: Built with reusable Python components
- **🔥 Hot Reload**: Development server with live updates
- **🎭 Lucide Icons**: Professional SVG icons throughout
- **🌈 Tailwind CSS**: Utility-first CSS framework via CDN
- **♿ Accessible**: Semantic HTML and proper ARIA labels

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- pip (Python package manager)

### Installation

1. **Clone or download this repository**

```bash
cd my-landing-page
```

2. **Create a virtual environment** (recommended)

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Snakeskin**

```bash
pip install snakeskin-xplnhub
```

4. **Install additional dependencies** (optional for hot reload)

```bash
pip install websockets
```

## 🛠️ Development

### Build the Project

Generate the static HTML file:

```bash
python3 main.py
```

This creates `dist/index.html` with all components rendered.

### Run Development Server

Start the dev server with hot reload:

```bash
snakeskin dev
```

Visit [http://localhost:3000/dist](http://localhost:3000/dist) to view your site.

### Build for Production

```bash
snakeskin build
```

## 📁 Project Structure

```
my-landing-page/
├── src/
│   └── components/
│       ├── Navbar.py          # Navigation bar with glass effect
│       ├── Hero.py            # Hero section with CTA
│       ├── Features.py        # Feature cards grid
│       ├── ContactForm.py     # Contact form with validation
│       └── Footer.py          # Footer with links
├── dist/
│   └── index.html            # Generated output
├── main.py                   # Entry point & HTML generator
├── input.css                 # Tailwind CSS input
├── tailwind.config.js        # Tailwind configuration
├── DEPLOYMENT.md            # Deployment guide
└── README.md                # This file
```

## 🎨 Components

### Navbar
- Glass morphism effect with backdrop blur
- Gradient logo with icon
- Responsive navigation links
- Glowing CTA button

### Hero Section
- Animated gradient background
- Version badge with sparkles icon
- Large, bold typography
- Dual CTA buttons (primary + secondary)
- Dashboard preview with glow effect

### Features
- 6 feature cards in responsive grid
- Gradient icon boxes
- Hover effects with shine animation
- Icons: Lightning, Palette, Wrench, Flame, Package, Rocket

### Contact Form
- Glass morphism card
- Gradient blob backgrounds
- Form validation
- Success state with icon
- Glowing submit button

### Footer
- Dark gradient background
- 4-column layout (responsive)
- Social media icons (Twitter, LinkedIn, Mail)
- Gradient text effects

## 🎭 Customization

### Change Colors

Edit the gradient colors in `main.py`:

```python
# Change from blue/indigo to your colors
bg-gradient-to-r from-blue-600 to-indigo-600
```

### Modify Components

Each component is a Python class in `src/components/`. Edit the `render()` method to change the HTML/styling:

```python
class Hero(Component):
    def render(self):
        return f"""
        <section class="...">
            <!-- Your custom HTML -->
        </section>
        """
```

### Add New Components

1. Create a new file in `src/components/`
2. Import it in `main.py`
3. Add it to the HTML output

```python
from src.components.NewComponent import NewComponent

new_component = NewComponent()
new_component.mount()

# Add to HTML
{new_component.render()}
```

### Change Icons

Icons use [Lucide](https://lucide.dev/). Browse available icons and replace:

```html
<i data-lucide="icon-name" style="width: 24px; height: 24px;"></i>
```

## 🌐 Deployment

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment instructions.

**Quick Deploy Options:**
- **Netlify Drop**: Drag & drop `dist` folder at [netlify.com/drop](https://app.netlify.com/drop)
- **Vercel**: `npm i -g vercel && vercel --prod`
- **GitHub Pages**: Push to GitHub and enable Pages in settings
- **Surge**: `npm i -g surge && cd dist && surge`

## 🔧 Technologies Used

- **[Snakeskin](https://github.com/xplnhub/snakeskin)**: Python web framework
- **[Tailwind CSS](https://tailwindcss.com/)**: Utility-first CSS framework
- **[Lucide Icons](https://lucide.dev/)**: Beautiful & consistent icon set
- **[Inter Font](https://fonts.google.com/specimen/Inter)**: Modern sans-serif typeface

## 📝 Scripts

| Command | Description |
|---------|-------------|
| `python3 main.py` | Build the static HTML file |
| `snakeskin dev` | Start development server |
| `snakeskin build` | Production build |
| `snakeskin --help` | View all available commands |

## 🎯 Performance

- **Static HTML**: No server-side rendering needed
- **CDN Resources**: Tailwind and Lucide loaded from CDN
- **Optimized CSS**: Only used Tailwind classes are included
- **Fast Load Time**: Minimal dependencies, maximum performance

## 🐛 Troubleshooting

### Build fails with "No module named 'snakeskin'"

Make sure you're in the virtual environment and Snakeskin is installed:

```bash
source venv/bin/activate
pip install snakeskin-xplnhub
```

### Icons not showing

Make sure the Lucide script is loading and `lucide.createIcons()` is called:

```html
<script src="https://unpkg.com/lucide@latest"></script>
<script>lucide.createIcons();</script>
```

### Styles not applying

Check that Tailwind CDN is loading in the `<head>`:

```html
<script src="https://cdn.tailwindcss.com"></script>
```

### Dev server shows empty page

Make sure you've built the project first:

```bash
python3 main.py
```

Then access the correct URL: `http://localhost:3000/dist/`

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 👨‍💻 Author

Built with 🐍 and ❤️ using Snakeskin via XplnHUB

## 🙏 Acknowledgments

- [Snakeskin Framework](https://github.com/xplnhub/snakeskin) by XplnHUB
- [Tailwind CSS](https://tailwindcss.com/) for the styling system
- [Lucide](https://lucide.dev/) for the beautiful icons
- [Inter Font](https://rsms.me/inter/) by Rasmus Andersson

---

**⭐ If you found this helpful, please consider giving it a star!**

For more information about Snakeskin, visit the [official documentation](https://github.com/xplnhub/snakeskin).
