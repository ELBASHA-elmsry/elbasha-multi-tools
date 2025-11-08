#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ELBASHA Multi Tools - Ultra Professional Mobile App
Advanced Material Design with Stunning Animations
Created by: ELBASHA
"""

from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton, MDIconButton, MDFillRoundFlatButton, MDRectangleFlatIconButton
from kivymd.uix.card import MDCard
from kivymd.uix.textfield import MDTextField
from kivy.uix.scrollview import ScrollView
from kivy.metrics import dp
from kivy.properties import StringProperty, NumericProperty, ListProperty
from kivy.graphics import Color, Rectangle, RoundedRectangle, Line, Ellipse
from kivy.animation import Animation
from kivy.clock import Clock
from datetime import datetime
import random

# ==================== ANIMATED BACKGROUND ====================
class AnimatedBackground(MDFloatLayout):
    """Stunning animated background with particles"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.particles = []
        self.bind(pos=self.update_canvas, size=self.update_canvas)
        Clock.schedule_once(lambda dt: self.setup_background(), 0.1)
        Clock.schedule_interval(self.animate_particles, 0.05)
    
    def setup_background(self):
        """Create gradient background with animated particles"""
        with self.canvas.before:
            # Gradient background (dark blue to purple)
            Color(0.05, 0.05, 0.15, 1)
            Rectangle(pos=self.pos, size=self.size)
            
            # Create floating particles
            for i in range(20):
                x = random.randint(0, int(self.width))
                y = random.randint(0, int(self.height))
                size = random.randint(2, 6)
                
                particle = {
                    'color': Color(
                        random.uniform(0.3, 0.7),
                        random.uniform(0.5, 0.9),
                        random.uniform(0.8, 1.0),
                        random.uniform(0.2, 0.5)
                    ),
                    'shape': Ellipse(pos=(x, y), size=(size, size)),
                    'velocity': [random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5)],
                    'size': size
                }
                self.particles.append(particle)
    
    def animate_particles(self, dt):
        """Animate floating particles"""
        for particle in self.particles:
            current_pos = particle['shape'].pos
            new_x = current_pos[0] + particle['velocity'][0]
            new_y = current_pos[1] + particle['velocity'][1]
            
            # Bounce off edges
            if new_x <= 0 or new_x >= self.width:
                particle['velocity'][0] *= -1
            if new_y <= 0 or new_y >= self.height:
                particle['velocity'][1] *= -1
            
            particle['shape'].pos = (new_x, new_y)
    
    def update_canvas(self, *args):
        pass


# ==================== GLASSMORPHISM CARD ====================
class GlassCard(MDCard):
    """Glassmorphism effect card"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.md_bg_color = (0.1, 0.1, 0.2, 0.3)
        self.elevation = 10
        self.radius = [20]
        
        with self.canvas.before:
            Color(1, 1, 1, 0.05)
            self.border = Line(
                rounded_rectangle=(self.x, self.y, self.width, self.height, 20),
                width=1.5
            )
        
        self.bind(pos=self.update_border, size=self.update_border)
    
    def update_border(self, *args):
        self.border.rounded_rectangle = (self.x, self.y, self.width, self.height, 20)


# ==================== HOME SCREEN WITH STUNNING UI ====================
class HomeScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Animated background
        bg = AnimatedBackground()
        self.add_widget(bg)
        
        # Main content
        content = MDFloatLayout()
        
        main_layout = MDBoxLayout(
            orientation='vertical',
            padding=dp(20),
            spacing=dp(25),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(1, 1)
        )
        
        # Logo and title with glow effect
        header_card = GlassCard(
            size_hint_y=None,
            height=dp(140),
            padding=dp(20)
        )
        
        header_layout = MDBoxLayout(orientation='vertical', spacing=dp(5))
        
        logo = MDLabel(
            text="💎",
            halign='center',
            font_style='H2',
            size_hint_y=0.5
        )
        header_layout.add_widget(logo)
        
        title = MDLabel(
            text="ELBASHA",
            halign='center',
            font_style='H3',
            size_hint_y=0.3,
            theme_text_color="Custom",
            text_color=(1, 0.85, 0.3, 1)
        )
        header_layout.add_widget(title)
        
        subtitle = MDLabel(
            text="Professional Multi Tools",
            halign='center',
            font_style='Subtitle1',
            size_hint_y=0.2,
            theme_text_color="Custom",
            text_color=(0.7, 0.8, 0.9, 1)
        )
        header_layout.add_widget(subtitle)
        
        header_card.add_widget(header_layout)
        main_layout.add_widget(header_card)
        
        # Menu buttons with enhanced design
        menu_layout = MDBoxLayout(orientation='vertical', spacing=dp(15), size_hint_y=1)
        
        tools = [
            {'name': 'Calculator', 'icon': 'calculator', 'color': (0.2, 0.5, 0.8, 1), 'screen': 'calculator'},
            {'name': 'Money Counter', 'icon': 'cash-multiple', 'color': (0.2, 0.7, 0.4, 1), 'screen': 'money'},
            {'name': 'Age Calculator', 'icon': 'calendar-heart', 'color': (0.9, 0.5, 0.3, 1), 'screen': 'age'}
        ]
        
        for tool in tools:
            btn_card = GlassCard(size_hint_y=None, height=dp(90), padding=dp(5))
            
            btn = MDRectangleFlatIconButton(
                text=tool['name'],
                icon=tool['icon'],
                line_color=tool['color'],
                text_color=(1, 1, 1, 1),
                icon_color=tool['color'],
                font_size='22sp',
                size_hint=(1, 1)
            )
            btn.bind(on_press=lambda x, s=tool['screen']: self.go_to_screen_animated(s))
            
            btn_card.add_widget(btn)
            menu_layout.add_widget(btn_card)
        
        main_layout.add_widget(menu_layout)
        
        # Footer
        footer = MDLabel(
            text="Version 2.0 | Made with ❤️",
            halign='center',
            font_style='Caption',
            size_hint_y=None,
            height=dp(30),
            theme_text_color="Custom",
            text_color=(0.5, 0.6, 0.7, 1)
        )
        main_layout.add_widget(footer)
        
        content.add_widget(main_layout)
        self.add_widget(content)
    
    def go_to_screen_animated(self, screen_name):
        self.manager.transition.direction = 'left'
        self.manager.current = screen_name


# ==================== CALCULATOR SCREEN ====================
class CalculatorScreen(MDScreen):
    expression = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        bg = AnimatedBackground()
        self.add_widget(bg)
        
        content = MDFloatLayout()
        main_layout = MDBoxLayout(orientation='vertical', padding=dp(15), spacing=dp(15))
        
        # Header with glass effect
        header_card = GlassCard(size_hint_y=None, height=dp(60), padding=dp(10))
        header = MDBoxLayout()
        
        back_btn = MDIconButton(
            icon="arrow-left-circle",
            icon_size="36sp",
            theme_text_color="Custom",
            text_color=(1, 0.85, 0.3, 1),
            size_hint_x=0.2
        )
        back_btn.bind(on_press=lambda x: self.go_back())
        header.add_widget(back_btn)
        
        title = MDLabel(
            text="Calculator",
            halign='center',
            font_style='H5',
            size_hint_x=0.6,
            theme_text_color="Custom",
            text_color=(1, 1, 1, 1)
        )
        header.add_widget(title)
        header.add_widget(MDLabel(size_hint_x=0.2))
        
        header_card.add_widget(header)
        main_layout.add_widget(header_card)
        
        # Display with glass effect
        display_card = GlassCard(size_hint_y=0.2, padding=dp(20))
        self.display_label = MDLabel(
            text="0",
            halign='right',
            font_style='H2',
            theme_text_color="Custom",
            text_color=(1, 0.85, 0.3, 1)
        )
        display_card.add_widget(self.display_label)
        main_layout.add_widget(display_card)
        self.bind(expression=self.update_display)
        
        # Buttons
        buttons_card = GlassCard(size_hint_y=0.7, padding=dp(15))
        buttons_grid = MDGridLayout(cols=4, spacing=dp(8))
        
        buttons = [
            ('7', (0.25, 0.35, 0.5, 1), False), ('8', (0.25, 0.35, 0.5, 1), False), 
            ('9', (0.25, 0.35, 0.5, 1), False), ('/', (0.3, 0.5, 0.7, 1), False),
            ('4', (0.25, 0.35, 0.5, 1), False), ('5', (0.25, 0.35, 0.5, 1), False), 
            ('6', (0.25, 0.35, 0.5, 1), False), ('*', (0.3, 0.5, 0.7, 1), False),
            ('1', (0.25, 0.35, 0.5, 1), False), ('2', (0.25, 0.35, 0.5, 1), False), 
            ('3', (0.25, 0.35, 0.5, 1), False), ('-', (0.3, 0.5, 0.7, 1), False),
            ('C', (0.8, 0.3, 0.3, 1), False), ('0', (0.25, 0.35, 0.5, 1), False), 
            ('=', (0.2, 0.7, 0.4, 1), False), ('+', (0.3, 0.5, 0.7, 1), False),
            ('⌫', (0.9, 0.5, 0.2, 1), True), ('', (0, 0, 0, 0), False), 
            ('', (0, 0, 0, 0), False), ('', (0, 0, 0, 0), False),
        ]
        
        for btn_text, color, is_backspace in buttons:
            if btn_text:
                if is_backspace:
                    # Create icon button for backspace
                    btn = MDIconButton(
                        icon="backspace-outline",
                        md_bg_color=color,
                        theme_text_color="Custom",
                        text_color=(1, 1, 1, 1),
                        icon_size="32sp"
                    )
                else:
                    # Create normal button
                    btn = MDRaisedButton(
                        text=btn_text,
                        md_bg_color=color,
                        font_size='26sp',
                        elevation=8
                    )
                
                btn.bind(on_press=lambda x, text=btn_text: self.button_press(text))
                buttons_grid.add_widget(btn)
            else:
                buttons_grid.add_widget(MDLabel())
        
        buttons_card.add_widget(buttons_grid)
        main_layout.add_widget(buttons_card)
        
        content.add_widget(main_layout)
        self.add_widget(content)
    
    def update_display(self, instance, value):
        self.display_label.text = value if value else "0"
    
    def button_press(self, button_text):
        if button_text == 'C':
            self.expression = ""
        elif button_text == '⌫':
            # Delete last character (Backspace icon style)
            if self.expression:
                self.expression = self.expression[:-1]
        elif button_text == '=':
            try:
                result = str(eval(self.expression))
                self.expression = result
            except Exception:
                self.expression = "Error"
        else:
            if self.expression == "Error":
                self.expression = ""
            self.expression += button_text
    
    def go_back(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'home'


# ==================== MONEY COUNTER SCREEN ====================
class MoneyCounterScreen(MDScreen):
    total_amount = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        bg = AnimatedBackground()
        self.add_widget(bg)
        
        self.currency_data = {
            200: {'count': 0, 'color': (0.9, 0.3, 0.2, 1), 'emoji': '💵'},
            100: {'count': 0, 'color': (0.8, 0.2, 0.5, 1), 'emoji': '💴'},
            50: {'count': 0, 'color': (0.2, 0.6, 0.9, 1), 'emoji': '💶'},
            20: {'count': 0, 'color': (0.3, 0.7, 0.3, 1), 'emoji': '💷'},
            10: {'count': 0, 'color': (0.9, 0.6, 0.2, 1), 'emoji': '💰'},
            5: {'count': 0, 'color': (0.6, 0.4, 0.8, 1), 'emoji': '🪙'},
            1: {'count': 0, 'color': (0.7, 0.7, 0.7, 1), 'emoji': '🔘'}
        }
        
        self.count_fields = {}
        self.subtotal_labels = {}
        
        content = MDFloatLayout()
        main_layout = MDBoxLayout(orientation='vertical', padding=dp(10), spacing=dp(10))
        
        # Header
        header_card = GlassCard(size_hint_y=None, height=dp(60), padding=dp(10))
        header = MDBoxLayout()
        
        back_btn = MDIconButton(
            icon="arrow-left-circle",
            icon_size="36sp",
            theme_text_color="Custom",
            text_color=(1, 0.85, 0.3, 1),
            size_hint_x=0.2
        )
        back_btn.bind(on_press=lambda x: self.go_back())
        header.add_widget(back_btn)
        
        title = MDLabel(
            text="Money Counter",
            halign='center',
            font_style='H5',
            size_hint_x=0.6
        )
        header.add_widget(title)
        header.add_widget(MDLabel(size_hint_x=0.2))
        
        header_card.add_widget(header)
        main_layout.add_widget(header_card)
        
        # Total card with glow
        total_card = GlassCard(
            size_hint_y=None,
            height=dp(100),
            padding=dp(15)
        )
        
        total_layout = MDBoxLayout(orientation='vertical', spacing=dp(5))
        
        total_title = MDLabel(
            text="💰 Total Money Calculator",
            halign="center",
            font_style="Subtitle1",
            size_hint_y=0.3
        )
        total_layout.add_widget(total_title)
        
        self.total_label = MDLabel(
            text="0 EGP",
            halign="center",
            font_style="H3",
            theme_text_color="Custom",
            text_color=(1, 0.85, 0.3, 1),
            size_hint_y=0.7
        )
        total_layout.add_widget(self.total_label)
        
        total_card.add_widget(total_layout)
        main_layout.add_widget(total_card)
        
        # Currency cards
        currency_layout = MDGridLayout(cols=1, spacing=dp(8), size_hint_y=1)
        
        for denom in [200, 100, 50, 20, 10, 5, 1]:
            card = MDCard(
                orientation="horizontal",
                padding=dp(8),
                spacing=dp(6),
                size_hint_y=1,
                md_bg_color=(*self.currency_data[denom]['color'][:3], 0.4),
                elevation=6,
                radius=[15]
            )
            
            # Info
            info_box = MDBoxLayout(orientation='vertical', size_hint_x=0.12, spacing=dp(2))
            emoji_label = MDLabel(
                text=self.currency_data[denom]['emoji'],
                halign="center",
                font_style="H6"
            )
            value_label = MDLabel(
                text=f"{denom}",
                halign="center",
                font_style="Caption",
                bold=True
            )
            info_box.add_widget(emoji_label)
            info_box.add_widget(value_label)
            card.add_widget(info_box)
            
            # Text input for count
            count_field = MDTextField(
                hint_text="0",
                text="",
                halign="center",
                font_size='20sp',
                size_hint_x=0.22,
                mode="rectangle",
                input_filter='int'
            )
            count_field.bind(
                text=lambda instance, value, d=denom: self.on_text_change(d, value),
                on_text_validate=lambda instance, d=denom: self.focus_next_money_field(d)
            )
            self.count_fields[denom] = count_field
            card.add_widget(count_field)
            
            # Buttons
            buttons_box = MDBoxLayout(size_hint_x=0.32, spacing=dp(4))
            
            minus_btn = MDIconButton(
                icon="minus-circle",
                theme_text_color="Custom",
                text_color=(1, 0.3, 0.3, 1),
                icon_size="28sp"
            )
            minus_btn.bind(on_press=lambda x, d=denom: self.update_count(d, -1))
            buttons_box.add_widget(minus_btn)
            
            plus_btn = MDIconButton(
                icon="plus-circle",
                theme_text_color="Custom",
                text_color=(0.3, 1, 0.3, 1),
                icon_size="28sp"
            )
            plus_btn.bind(on_press=lambda x, d=denom: self.update_count(d, 1))
            buttons_box.add_widget(plus_btn)
            
            card.add_widget(buttons_box)
            
            # Subtotal
            subtotal_label = MDLabel(
                text="0",
                halign="center",
                font_style="Caption",
                size_hint_x=0.34,
                bold=True
            )
            self.subtotal_labels[denom] = subtotal_label
            card.add_widget(subtotal_label)
            
            currency_layout.add_widget(card)
        
        main_layout.add_widget(currency_layout)
        
        # Reset button
        reset_card = GlassCard(size_hint_y=None, height=dp(55), padding=dp(5))
        reset_btn = MDFillRoundFlatButton(
            text="🔄 Reset All",
            size_hint=(1, 1),
            md_bg_color=(0.8, 0.3, 0.2, 1),
            font_size='18sp'
        )
        reset_btn.bind(on_press=self.clear_all)
        reset_card.add_widget(reset_btn)
        main_layout.add_widget(reset_card)
        
        content.add_widget(main_layout)
        self.add_widget(content)
    
    def on_text_change(self, denomination, value):
        try:
            count = int(value) if value else 0
            self.currency_data[denomination]['count'] = count
            self.calculate_total()
        except ValueError:
            pass
    
    def focus_next_money_field(self, current_denom):
        """Move to next denomination field when Enter is pressed"""
        denoms = [200, 100, 50, 20, 10, 5, 1]
        try:
            current_index = denoms.index(current_denom)
            if current_index < len(denoms) - 1:
                next_denom = denoms[current_index + 1]
                self.count_fields[next_denom].focus = True
        except (ValueError, IndexError):
            pass
    
    def update_count(self, denomination, change):
        current = self.currency_data[denomination]['count']
        new_count = max(0, current + change)
        self.currency_data[denomination]['count'] = new_count
        self.count_fields[denomination].text = str(new_count) if new_count > 0 else ""
        self.calculate_total()
    
    def calculate_total(self):
        total = sum(d * data['count'] for d, data in self.currency_data.items())
        self.total_amount = total
        self.total_label.text = f"{int(total):,} EGP".replace(',', '.')
        
        # Update subtotals
        for denom in self.currency_data:
            subtotal = denom * self.currency_data[denom]['count']
            self.subtotal_labels[denom].text = f"{subtotal:,}".replace(',', '.')
    
    def clear_all(self, instance=None):
        for denomination in self.currency_data:
            self.currency_data[denomination]['count'] = 0
            self.count_fields[denomination].text = ''
            self.subtotal_labels[denomination].text = '0'
        self.calculate_total()
    
    def go_back(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'home'


# ==================== AGE CALCULATOR SCREEN ====================
class AgeCalculatorScreen(MDScreen):
    age_result = StringProperty("")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        bg = AnimatedBackground()
        self.add_widget(bg)
        
        content = MDFloatLayout()
        main_layout = MDBoxLayout(orientation='vertical', padding=dp(20), spacing=dp(15))
        
        # Header
        header_card = GlassCard(size_hint_y=None, height=dp(60), padding=dp(10))
        header = MDBoxLayout()
        
        back_btn = MDIconButton(
            icon="arrow-left-circle",
            icon_size="36sp",
            theme_text_color="Custom",
            text_color=(1, 0.85, 0.3, 1),
            size_hint_x=0.2
        )
        back_btn.bind(on_press=lambda x: self.go_back())
        header.add_widget(back_btn)
        
        title = MDLabel(
            text="Age Calculator",
            halign='center',
            font_style='H5',
            size_hint_x=0.6
        )
        header.add_widget(title)
        header.add_widget(MDLabel(size_hint_x=0.2))
        
        header_card.add_widget(header)
        main_layout.add_widget(header_card)
        
        # Input card
        input_card = GlassCard(padding=dp(20), spacing=dp(15), size_hint_y=0.55)
        
        input_layout = MDBoxLayout(orientation='vertical', spacing=dp(15))
        
        input_title = MDLabel(
            text="📅 Enter Birth Date",
            halign='center',
            font_style='H6',
            size_hint_y=None,
            height=dp(40),
            theme_text_color="Custom",
            text_color=(1, 0.85, 0.3, 1)
        )
        input_layout.add_widget(input_title)
        
        # Day field (first)
        self.day_field = MDTextField(
            hint_text="Day (1-31)",
            mode="rectangle",
            size_hint_y=None,
            height=dp(60),
            font_size='20sp',
            input_filter='int'
        )
        self.day_field.bind(on_text_validate=self.focus_next_field)
        input_layout.add_widget(self.day_field)
        
        # Month field (second)
        self.month_field = MDTextField(
            hint_text="Month (1-12)",
            mode="rectangle",
            size_hint_y=None,
            height=dp(60),
            font_size='20sp',
            input_filter='int'
        )
        self.month_field.bind(on_text_validate=self.focus_next_field)
        input_layout.add_widget(self.month_field)
        
        # Year field (third)
        self.year_field = MDTextField(
            hint_text="Year (e.g., 2000)",
            mode="rectangle",
            size_hint_y=None,
            height=dp(60),
            font_size='20sp',
            input_filter='int'
        )
        self.year_field.bind(on_text_validate=lambda x: self.calculate_age())
        input_layout.add_widget(self.year_field)
        
        calc_btn = MDRaisedButton(
            text="✨ Calculate Age",
            size_hint_y=None,
            height=dp(65),
            md_bg_color=(0.2, 0.7, 0.4, 1),
            font_size='20sp',
            elevation=8
        )
        calc_btn.bind(on_press=self.calculate_age)
        input_layout.add_widget(calc_btn)
        
        input_card.add_widget(input_layout)
        main_layout.add_widget(input_card)
        
        # Result card
        result_card = GlassCard(padding=dp(20), size_hint_y=0.35)
        
        self.result_label = MDLabel(
            text="Your age will appear here ✨",
            halign='center',
            font_style='H5',
            theme_text_color="Custom",
            text_color=(1, 0.85, 0.3, 1)
        )
        self.bind(age_result=lambda instance, value: setattr(self.result_label, 'text', value))
        result_card.add_widget(self.result_label)
        
        main_layout.add_widget(result_card)
        
        content.add_widget(main_layout)
        self.add_widget(content)
    
    def focus_next_field(self, instance):
        """Move focus to next field when Enter is pressed"""
        if instance == self.day_field:
            self.month_field.focus = True
        elif instance == self.month_field:
            self.year_field.focus = True
    
    def calculate_age(self, instance=None):
        try:
            day = int(self.day_field.text) if self.day_field.text else 1
            month = int(self.month_field.text) if self.month_field.text else 1
            year = int(self.year_field.text) if self.year_field.text else 2000
            
            birth_date = datetime(year, month, day)
            today = datetime.now()
            
            age_years = today.year - birth_date.year
            age_months = today.month - birth_date.month
            age_days = today.day - birth_date.day
            
            if age_days < 0:
                age_months -= 1
                age_days += 30
            if age_months < 0:
                age_years -= 1
                age_months += 12
            
            self.age_result = f"🎂 Your Age:\n\n{age_years} Years ✨\n{age_months} Months 🌙\n{age_days} Days ⭐"
            
        except ValueError:
            self.age_result = "❌ Invalid Date!\nPlease check your input"
        except Exception:
            self.age_result = "⚠️ Error occurred!"
    
    def go_back(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'home'


# ==================== MAIN APP ====================
class ElbashaApp(MDApp):
    def build(self):
        self.title = "ELBASHA Multi Tools Pro"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.accent_palette = "Amber"
        
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(CalculatorScreen(name='calculator'))
        sm.add_widget(MoneyCounterScreen(name='money'))
        sm.add_widget(AgeCalculatorScreen(name='age'))
        
        return sm


if __name__ == "__main__":
    ElbashaApp().run()