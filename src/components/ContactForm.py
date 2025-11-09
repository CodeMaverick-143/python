from snakeskin.framework import Component

class ContactForm(Component):
    def __init__(self, **props):
        super().__init__(**props)
        self.state = {
            "name": "",
            "email": "",
            "message": "",
            "submitted": False,
            "errors": {}
        }
    
    def validate_form(self):
        errors = {}
        if not self.state.get("name"):
            errors["name"] = "Name is required"
        if not self.state.get("email"):
            errors["email"] = "Email is required"
        elif "@" not in self.state.get("email", ""):
            errors["email"] = "Invalid email format"
        if not self.state.get("message"):
            errors["message"] = "Message is required"
        return errors
    
    def render(self):
        submitted = self.state.get("submitted", False)
        
        if submitted:
            return f"""
            <section id="contact" class="py-20 bg-gradient-to-br from-blue-50 to-indigo-100">
                <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div class="bg-white rounded-xl shadow-lg p-12 text-center">
                        <div class="mb-4 inline-block">
                            <div class="bg-green-100 p-6 rounded-full">
                                <i data-lucide="check-circle" class="text-green-600" style="width: 48px; height: 48px;"></i>
                            </div>
                        </div>
                        <h3 class="text-3xl font-bold text-gray-900 mb-4">Thank You!</h3>
                        <p class="text-xl text-gray-600">We'll get back to you soon.</p>
                    </div>
                </div>
            </section>
            """
        
        return f"""
        <section id="contact" class="py-24 bg-gradient-to-br from-blue-50 via-indigo-50 to-purple-50 relative overflow-hidden">
            <div class="absolute inset-0 opacity-30">
                <div class="absolute top-0 left-0 w-96 h-96 bg-blue-300 rounded-full filter blur-3xl"></div>
                <div class="absolute bottom-0 right-0 w-96 h-96 bg-purple-300 rounded-full filter blur-3xl"></div>
            </div>
            <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
                <div class="text-center mb-16 fade-in-up">
                    <h2 class="text-5xl font-black text-gray-900 mb-6">Get In Touch</h2>
                    <p class="text-2xl text-gray-600">Have questions? We'd love to hear from you.</p>
                </div>
                <div class="glass rounded-2xl shadow-2xl p-10 hover-lift">
                    <form onsubmit="handleSubmit_{id(self)}(event)" class="space-y-6">
                        <div>
                            <label class="block text-gray-800 font-bold mb-3 text-lg">Name</label>
                            <input 
                                type="text" 
                                name="name"
                                class="w-full px-5 py-4 border-2 border-gray-200 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition text-lg"
                                placeholder="Your name"
                                required
                            />
                        </div>
                        <div>
                            <label class="block text-gray-800 font-bold mb-3 text-lg">Email</label>
                            <input 
                                type="email" 
                                name="email"
                                class="w-full px-5 py-4 border-2 border-gray-200 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition text-lg"
                                placeholder="your.email@example.com"
                                required
                            />
                        </div>
                        <div>
                            <label class="block text-gray-800 font-bold mb-3 text-lg">Message</label>
                            <textarea 
                                name="message"
                                rows="5"
                                class="w-full px-5 py-4 border-2 border-gray-200 rounded-xl focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition text-lg resize-none"
                                placeholder="Tell us what you're thinking..."
                                required
                            ></textarea>
                        </div>
                        <button 
                            type="submit"
                            class="w-full bg-gradient-to-r from-blue-600 to-indigo-600 text-white px-8 py-5 rounded-xl text-xl font-bold btn-glow shadow-2xl flex items-center justify-center gap-3"
                        >
                            Send Message
                            <i data-lucide="send" style="width: 24px; height: 24px;"></i>
                        </button>
                    </form>
                </div>
            </div>
            <script>
                function handleSubmit_{id(self)}(event) {{
                    event.preventDefault();
                    const formData = new FormData(event.target);
                    console.log("Form submitted:", Object.fromEntries(formData));
                    alert("Thank you for your message! We'll get back to you soon.");
                    event.target.reset();
                }}
            </script>
        </section>
        """