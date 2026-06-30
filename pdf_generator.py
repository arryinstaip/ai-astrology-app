print("HELLO FROM PDF_GENERATOR")
"""
PDF Generator Module
--------------------
Creates downloadable PDF reports using ReportLab.
"""

from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black, white
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
import io
from datetime import datetime


class PDFGenerator:
    """Generates formatted PDF reports for astrology readings."""
    
    def __init__(self):
        """Initialize PDF generator with custom styles."""
        self.styles = getSampleStyleSheet()
        self._create_custom_styles()
    
    def _create_custom_styles(self):
        """Create custom paragraph styles for the PDF."""
        # Title style
        self.styles.add(ParagraphStyle(
            name='CustomTitle',
            parent=self.styles['Heading1'],
            fontSize=24,
            spaceAfter=30,
            alignment=TA_CENTER,
            textColor=HexColor('#C9A227')  # Gold color
        ))
        
        # Section header style
        self.styles.add(ParagraphStyle(
            name='SectionHeader',
            parent=self.styles['Heading2'],
            fontSize=14,
            spaceBefore=20,
            spaceAfter=10,
            textColor=HexColor('#C9A227')
        ))
        
        # Body text style
        self.styles.add(ParagraphStyle(
            name='CustomBodyText',
            parent=self.styles['Normal'],
            fontSize=11,
            spaceAfter=12,
            alignment=TA_JUSTIFY,
            leading=14
        ))
        
        # Highlight style for key information
        self.styles.add(ParagraphStyle(
            name='Highlight',
            parent=self.styles['Normal'],
            fontSize=12,
            spaceBefore=6,
            spaceAfter=6,
            textColor=HexColor('#4A90A4')
        ))
    
    def create_pdf(self, user_data: dict, astrology_data: dict, report: dict) -> io.BytesIO:
        """
        Create a complete PDF report.
        
        Args:
            user_data: User's personal information
            astrology_data: Calculated astrological data
            report: Generated report content
            
        Returns:
            BytesIO buffer containing the PDF
        """
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(
            buffer,
            pagesize=A4,
            rightMargin=0.75*inch,
            leftMargin=0.75*inch,
            topMargin=0.75*inch,
            bottomMargin=0.75*inch
        )
        
        # Build the PDF content
        story = []
        
        # Title
        story.append(Paragraph("✧ Astrology Report ✧", self.styles['CustomTitle']))
        story.append(Spacer(1, 10))
        
        # User information
        story.append(Paragraph(f"Prepared for: {user_data.get('full_name', 'Guest')}", self.styles['Highlight']))
        story.append(Paragraph(f"Generated: {datetime.now().strftime('%B %d, %Y')}", self.styles['CustomBodyText']))
        story.append(Spacer(1, 20))
        
        # Zodiac Summary
        story.append(Paragraph("Your Cosmic Profile", self.styles['SectionHeader']))
        
        zodiac_info = [
            ['Zodiac Sign', f"{astrology_data.get('zodiac_sign', 'Unknown')} {astrology_data.get('zodiac_symbol', '')}"],
            ['Element', astrology_data.get('element', 'Unknown')],
            ['Chinese Zodiac', f"{astrology_data.get('chinese_zodiac', 'Unknown')} {astrology_data.get('chinese_symbol', '')}"],
            ['Lucky Number', str(astrology_data.get('lucky_number', ''))],
            ['Lucky Color', astrology_data.get('lucky_color', '')],
            ['Lucky Day', astrology_data.get('lucky_day', '')],
            ['Lucky Gemstone', astrology_data.get('lucky_gemstone', '')],
            ['Life Path Number', str(astrology_data.get('life_path_number', ''))]
        ]
        
        table = Table(zodiac_info, colWidths=[2*inch, 4*inch])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, -1), HexColor('#1a1a2e')),
            ('TEXTCOLOR', (0, 0), (0, -1), HexColor('#C9A227')),
            ('TEXTCOLOR', (1, 0), (1, -1), black),
            ('FONTSIZE', (0, 0), (-1, -1), 11),
            ('PADDING', (0, 0), (-1, -1), 8),
            ('GRID', (0, 0), (-1, -1), 0.5, HexColor('#333333'))
        ]))
        story.append(table)
        story.append(Spacer(1, 20))
        
        # Personality Overview
        story.append(Paragraph("Personality Overview", self.styles['SectionHeader']))
        story.append(Paragraph(report.get('personality_overview', ''), self.styles['CustomBodyText']))
        story.append(Spacer(1, 10))
        
        # Strengths
        story.append(Paragraph("Your Strengths", self.styles['SectionHeader']))
        strengths = report.get('strengths', [])
        strengths_text = ' • '.join(strengths) if strengths else 'Not available'
        story.append(Paragraph(strengths_text, self.styles['CustomBodyText']))
        
        # Weaknesses
        story.append(Paragraph("Areas for Growth", self.styles['SectionHeader']))
        weaknesses = report.get('weaknesses', [])
        weaknesses_text = ' • '.join(weaknesses) if weaknesses else 'Not available'
        story.append(Paragraph(weaknesses_text, self.styles['CustomBodyText']))
        
        # Hidden Talents
        story.append(Paragraph("Hidden Talents", self.styles['SectionHeader']))
        talents = report.get('hidden_talents', [])
        talents_text = ' • '.join(talents) if talents else 'Not available'
        story.append(Paragraph(talents_text, self.styles['CustomBodyText']))
        
        # Career Suggestions
        story.append(Paragraph("Career Guidance", self.styles['SectionHeader']))
        careers = report.get('career_suggestions', [])
        for career in careers[:6]:
            story.append(Paragraph(f"• {career}", self.styles['CustomBodyText']))
        
        # Financial Outlook
        story.append(Paragraph("Financial Outlook", self.styles['SectionHeader']))
        story.append(Paragraph(report.get('financial_outlook', ''), self.styles['CustomBodyText']))
        
        # Relationship Insights
        story.append(Paragraph("Relationship Insights", self.styles['SectionHeader']))
        story.append(Paragraph(report.get('relationship_insights', ''), self.styles['CustomBodyText']))
        
        # Marriage Compatibility
        compatibility = report.get('marriage_compatibility', {})
        if compatibility.get('most_compatible'):
            story.append(Paragraph("Most Compatible Signs", self.styles['SectionHeader']))
            story.append(Paragraph(', '.join(compatibility['most_compatible']), self.styles['CustomBodyText']))
        
        # Health & Wellness
        story.append(Paragraph("Health & Wellness", self.styles['SectionHeader']))
        health = report.get('health_wellness', {})
        story.append(Paragraph(health.get('wellness_tips', ''), self.styles['CustomBodyText']))
        
        # Monthly Horoscope
        story.append(Paragraph("Monthly Horoscope", self.styles['SectionHeader']))
        story.append(Paragraph(report.get('monthly_horoscope', ''), self.styles['CustomBodyText']))
        
        # Daily Quote
        story.append(Spacer(1, 20))
        story.append(Paragraph("✧ Daily Inspiration ✧", self.styles['SectionHeader']))
        story.append(Paragraph(f'"{report.get("daily_quote", "")}"', self.styles['Highlight']))
        
        # Disclaimer
        story.append(Spacer(1, 30))
        disclaimer_style = ParagraphStyle(
            name='Disclaimer',
            parent=self.styles['Normal'],
            fontSize=9,
            textColor=HexColor('#666666'),
            alignment=TA_CENTER
        )
        story.append(Paragraph(report.get('disclaimer', ''), disclaimer_style))
        
        # Build the PDF
        doc.build(story)
        buffer.seek(0)
        
        return buffer
