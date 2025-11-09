from src.components.Navbar import Navbar
from src.components.Hero import Hero
from src.components.Features import Features
from src.components.ContactForm import ContactForm
from src.components.Footer import Footer

# Initialize components
navbar = Navbar()
hero = Hero()
features = Features()
contact = ContactForm()
footer = Footer()

# Mount components to activate lifecycle hooks
navbar.mount()
hero.mount()
features.mount()
contact.mount()
footer.mount()

# Create HTML content
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Snakeskin - Modern Python Web Framework</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        html {{
            scroll-behavior: smooth;
        }}
        
        body {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
        }}
        
        /* Gradient animations */
        @keyframes gradient {{
            0% {{ background-position: 0% 50%; }}
            50% {{ background-position: 100% 50%; }}
            100% {{ background-position: 0% 50%; }}
        }}
        
        .gradient-animate {{
            background-size: 200% 200%;
            animation: gradient 15s ease infinite;
        }}
        
        /* Smooth hover effects */
        .hover-lift {{
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }}
        
        .hover-lift:hover {{
            transform: translateY(-8px);
            box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
        }}
        
        /* Glass morphism effect */
        .glass {{
            background: rgba(255, 255, 255, 0.9);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.2);
        }}
        
        /* Custom button glow */
        .btn-glow {{
            box-shadow: 0 0 20px rgba(59, 130, 246, 0.5);
            transition: all 0.3s ease;
        }}
        
        .btn-glow:hover {{
            box-shadow: 0 0 30px rgba(59, 130, 246, 0.8);
            transform: translateY(-2px);
        }}
        
        /* Fade in animation */
        @keyframes fadeInUp {{
            from {{
                opacity: 0;
                transform: translateY(30px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}
        
        .fade-in-up {{
            animation: fadeInUp 0.8s ease-out;
        }}
        
        /* Feature card hover effect */
        .feature-card {{
            transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            overflow: hidden;
        }}
        
        .feature-card::before {{
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(59, 130, 246, 0.1), transparent);
            transition: left 0.5s;
        }}
        
        .feature-card:hover::before {{
            left: 100%;
        }}
        
        .feature-card:hover {{
            transform: translateY(-10px) scale(1.02);
            box-shadow: 0 25px 50px rgba(0, 0, 0, 0.15);
        }}
    </style>
</head>
<body class="bg-gradient-to-br from-gray-50 via-blue-50 to-indigo-50">
    {navbar.render()}
    {hero.render()}
    {features.render()}
    {contact.render()}
    {footer.render()}
    <script>
        lucide.createIcons();
    </script>
</body>
</html>
"""

# Write to file
with open("dist/index.html", "w") as f:
    f.write(html_content)

print("✅ Build complete! Open dist/index.html to view your landing page.")