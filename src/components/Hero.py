from snakeskin.framework import Component

class Hero(Component):
    def __init__(self, **props):
        super().__init__(**props)
        self.state = {
            "button_clicked": False,
            "email": ""
        }
    
    def handle_click(self):
        self.set_state({"button_clicked": True})
    
    def render(self):
        clicked = self.state.get("button_clicked", False)
        button_icon = '<i data-lucide="party-popper" style="width: 20px; height: 20px;"></i>' if clicked else '<i data-lucide="rocket" style="width: 20px; height: 20px;"></i>'
        button_text = "Thanks for your interest!" if clicked else "Get Started Free"
        button_class = "bg-green-500 hover:bg-green-600" if clicked else "bg-blue-600 hover:bg-blue-700"
        
        return f"""
        <section class="pt-32 pb-20 min-h-screen flex items-center relative overflow-hidden">
            <div class="absolute inset-0 bg-gradient-to-br from-blue-50 via-indigo-50 to-purple-50 gradient-animate"></div>
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
                <div class="text-center fade-in-up">
                    <div class="inline-block mb-4">
                        <span class="bg-blue-100 text-blue-700 px-4 py-2 rounded-full text-sm font-semibold flex items-center gap-2 justify-center">
                            <i data-lucide="sparkles" style="width: 16px; height: 16px;"></i>
                            New: Version 1.0 Released
                        </span>
                    </div>
                    <h1 class="text-5xl md:text-7xl font-black text-gray-900 mb-6 leading-tight">
                        Build Modern Web Apps<br/>
                        <span class="bg-gradient-to-r from-blue-600 via-indigo-600 to-purple-600 bg-clip-text text-transparent">
                            Venomously Fast
                        </span>
                    </h1>
                    <p class="text-xl md:text-2xl text-gray-600 mb-10 max-w-3xl mx-auto leading-relaxed">
                        Snakeskin is a lightweight Python framework for building component-based 
                        web applications with Tailwind CSS integration and hot reload.
                    </p>
                    <div class="flex flex-col sm:flex-row gap-4 justify-center items-center mb-16">
                        <button 
                            onclick="handleHeroClick_{id(self)}()"
                            class="bg-gradient-to-r from-blue-600 to-indigo-600 text-white px-10 py-5 rounded-xl text-lg font-bold btn-glow shadow-2xl flex items-center gap-3"
                        >
                            {button_icon}
                            {button_text}
                        </button>
                        <a href="#features" class="text-gray-700 px-10 py-5 rounded-xl text-lg font-semibold hover:bg-white/50 transition backdrop-blur-sm border-2 border-gray-200 flex items-center gap-2">
                            Learn More
                            <i data-lucide="arrow-down" style="width: 20px; height: 20px;"></i>
                        </a>
                    </div>
                    <div class="mt-12 hover-lift">
                        <div class="relative inline-block">
                            <div class="absolute inset-0 bg-gradient-to-r from-blue-400 to-purple-400 rounded-2xl blur-2xl opacity-30"></div>
                            <img src="https://via.placeholder.com/900x500/4F46E5/FFFFFF?text=Dashboard+Preview" 
                                 alt="Dashboard Preview" 
                                 class="rounded-2xl shadow-2xl mx-auto relative border-4 border-white"
                            />
                        </div>
                    </div>
                </div>
            </div>
            <script>
                function handleHeroClick_{id(self)}() {{
                    console.log("Hero button clicked!");
                    // In production, you would make an API call here
                }}
            </script>
        </section>
        """