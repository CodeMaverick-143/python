from snakeskin.framework import Component

class Features(Component):
    def __init__(self, **props):
        super().__init__(**props)
        self.features = [
            {
                "icon": "zap",
                "title": "Lightning Fast",
                "description": "Build and deploy web applications in minutes, not hours."
            },
            {
                "icon": "palette",
                "title": "Beautiful UI",
                "description": "Integrated with Tailwind CSS for stunning, responsive designs."
            },
            {
                "icon": "wrench",
                "title": "Easy to Use",
                "description": "Simple Python syntax with powerful component-based architecture."
            },
            {
                "icon": "flame",
                "title": "Hot Reload",
                "description": "See your changes instantly with built-in development server."
            },
            {
                "icon": "package",
                "title": "Component-Based",
                "description": "Build reusable components with state management and lifecycle hooks."
            },
            {
                "icon": "rocket",
                "title": "Deploy Anywhere",
                "description": "Deploy to Vercel, Netlify, or any static hosting platform."
            }
        ]
    
    def render(self):
        features_html = ""
        for feature in self.features:
            features_html += f"""
            <div class="feature-card bg-white p-8 rounded-2xl shadow-xl border border-gray-100">
                <div class="mb-6 transform transition-transform hover:scale-110 inline-block">
                    <div class="bg-gradient-to-br from-blue-500 to-indigo-600 p-4 rounded-xl">
                        <i data-lucide="{feature['icon']}" class="text-white" style="width: 32px; height: 32px;"></i>
                    </div>
                </div>
                <h3 class="text-2xl font-bold text-gray-900 mb-4">{feature['title']}</h3>
                <p class="text-gray-600 leading-relaxed">{feature['description']}</p>
            </div>
            """
        
        return f"""
        <section id="features" class="py-24 bg-white relative">
            <div class="absolute inset-0 bg-gradient-to-b from-transparent via-blue-50/30 to-transparent"></div>
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
                <div class="text-center mb-20 fade-in-up">
                    <h2 class="text-5xl font-black text-gray-900 mb-6">Why Choose Snakeskin?</h2>
                    <p class="text-2xl text-gray-600">Everything you need to build modern web applications</p>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                    {features_html}
                </div>
            </div>
        </section>
        """