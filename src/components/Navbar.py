from snakeskin.framework import Component

class Navbar(Component):
    def __init__(self, **props):
        super().__init__(**props)
        self.state = {
            "mobile_menu_open": False
        }
    
    def toggle_menu(self):
        self.set_state({"mobile_menu_open": not self.state.get("mobile_menu_open", False)})
    
    def render(self):
        menu_open = self.state.get("mobile_menu_open", False)
        
        return f"""
        <nav class="glass fixed w-full top-0 z-50 shadow-lg">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <div class="flex justify-between h-16">
                    <div class="flex items-center">
                        <h1 class="text-2xl font-bold bg-gradient-to-r from-blue-600 to-indigo-600 bg-clip-text text-transparent">🐍 Snakeskin</h1>
                    </div>
                    <div class="hidden md:flex items-center space-x-8">
                        <a href="#features" class="text-gray-700 hover:text-blue-600 transition font-medium">Features</a>
                        <a href="#about" class="text-gray-700 hover:text-blue-600 transition font-medium">About</a>
                        <a href="#contact" class="text-gray-700 hover:text-blue-600 transition font-medium">Contact</a>
                        <button class="bg-gradient-to-r from-blue-600 to-indigo-600 text-white px-6 py-2 rounded-lg btn-glow font-semibold flex items-center gap-2">
                            Get Started
                            <i data-lucide="arrow-right" style="width: 18px; height: 18px;"></i>
                        </button>
                    </div>
                </div>
            </div>
        </nav>
        """