from snakeskin.framework import Component

class Footer(Component):
    def render(self):
        return f"""
        <footer class="bg-gradient-to-br from-gray-900 via-gray-800 to-gray-900 text-white py-16 relative overflow-hidden">
            <div class="absolute inset-0 opacity-10">
                <div class="absolute top-0 right-0 w-96 h-96 bg-blue-500 rounded-full filter blur-3xl"></div>
                <div class="absolute bottom-0 left-0 w-96 h-96 bg-purple-500 rounded-full filter blur-3xl"></div>
            </div>
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
                <div class="grid grid-cols-1 md:grid-cols-4 gap-12 mb-12">
                    <div>
                        <div class="flex items-center gap-2 mb-4">
                            <i data-lucide="zap" class="text-blue-400" style="width: 28px; height: 28px;"></i>
                            <h3 class="text-2xl font-black bg-gradient-to-r from-blue-400 to-purple-400 bg-clip-text text-transparent">Snakeskin</h3>
                        </div>
                        <p class="text-gray-300 leading-relaxed">
                            A modern Python framework for building beautiful web applications with speed and elegance.
                        </p>
                    </div>
                    <div>
                        <h4 class="font-bold mb-4 text-lg text-white">Product</h4>
                        <ul class="space-y-3 text-gray-300">
                            <li><a href="#features" class="hover:text-blue-400 transition-colors">Features</a></li>
                            <li><a href="#" class="hover:text-blue-400 transition-colors">Pricing</a></li>
                            <li><a href="#" class="hover:text-blue-400 transition-colors">Documentation</a></li>
                        </ul>
                    </div>
                    <div>
                        <h4 class="font-bold mb-4 text-lg text-white">Company</h4>
                        <ul class="space-y-3 text-gray-300">
                            <li><a href="#about" class="hover:text-blue-400 transition-colors">About</a></li>
                            <li><a href="#" class="hover:text-blue-400 transition-colors">Blog</a></li>
                            <li><a href="#contact" class="hover:text-blue-400 transition-colors">Contact</a></li>
                        </ul>
                    </div>
                    <div>
                        <h4 class="font-bold mb-4 text-lg text-white">Connect</h4>
                        <div class="flex space-x-4">
                            <a href="#" class="text-gray-300 hover:text-blue-400 transition-all transform hover:scale-125">
                                <i data-lucide="twitter" style="width: 28px; height: 28px;"></i>
                            </a>
                            <a href="#" class="text-gray-300 hover:text-blue-400 transition-all transform hover:scale-125">
                                <i data-lucide="linkedin" style="width: 28px; height: 28px;"></i>
                            </a>
                            <a href="#" class="text-gray-300 hover:text-blue-400 transition-all transform hover:scale-125">
                                <i data-lucide="mail" style="width: 28px; height: 28px;"></i>
                            </a>
                        </div>
                    </div>
                </div>
                <div class="border-t border-gray-700 pt-8 text-center">
                    <p class="text-gray-400 text-lg flex items-center justify-center gap-2">
                        &copy; 2025 Snakeskin via XplnHUB. Built with 
                        <i data-lucide="code" style="width: 18px; height: 18px;"></i>
                        and
                        <i data-lucide="heart" class="text-red-400" style="width: 18px; height: 18px;"></i>
                    </p>
                </div>
            </div>
        </footer>
        """