print("HELLO FROM REPORT_GENERATOR")
"""
Report Generator Module
-----------------------
Generates personalized astrology reports based on calculated data.
All interpretations are symbolic and for entertainment purposes.
"""

import random
from datetime import datetime


class ReportGenerator:
    """
    Generates comprehensive astrology reports with personalized insights.
    All content is symbolic interpretation, not factual prediction.
    """
    
    def __init__(self):
        """Initialize the report generator with template data."""
        self._load_templates()
    
    def _load_templates(self):
        """Load all template text for report generation."""
        
        # Personality traits by zodiac sign
        self.personality_traits = {
            'Aries': {
                'overview': "You possess a dynamic and pioneering spirit. Your natural leadership abilities and enthusiasm inspire those around you. With Mars as your ruling planet, you approach life with courage and determination.",
                'strengths': ['Natural leader', 'Courageous', 'Enthusiastic', 'Optimistic', 'Honest', 'Passionate'],
                'weaknesses': ['Impatient', 'Short-tempered', 'Impulsive', 'Aggressive at times', 'Competitive'],
                'hidden_talents': ['Crisis management', 'Sports and athletics', 'Entrepreneurship', 'Motivational speaking']
            },
            'Taurus': {
                'overview': "You embody stability, reliability, and a deep appreciation for life's pleasures. Ruled by Venus, you have an innate sense of beauty and a strong connection to the material world.",
                'strengths': ['Reliable', 'Patient', 'Practical', 'Devoted', 'Responsible', 'Stable'],
                'weaknesses': ['Stubborn', 'Possessive', 'Uncompromising', 'Resistant to change'],
                'hidden_talents': ['Financial management', 'Culinary arts', 'Music and singing', 'Gardening']
            },
            'Gemini': {
                'overview': "Your mind is your greatest asset—quick, versatile, and endlessly curious. Ruled by Mercury, you excel at communication and thrive on intellectual stimulation and variety.",
                'strengths': ['Adaptable', 'Outgoing', 'Intelligent', 'Curious', 'Versatile', 'Witty'],
                'weaknesses': ['Indecisive', 'Nervous', 'Inconsistent', 'Superficial at times'],
                'hidden_talents': ['Writing and journalism', 'Teaching', 'Sales and negotiation', 'Languages']
            },
            'Cancer': {
                'overview': "You possess deep emotional intelligence and nurturing instincts. Ruled by the Moon, your intuition is remarkably strong, and you create a sense of home wherever you go.",
                'strengths': ['Loyal', 'Emotional intelligence', 'Caring', 'Protective', 'Intuitive', 'Creative'],
                'weaknesses': ['Moody', 'Overly sensitive', 'Clingy', 'Self-protective', 'Suspicious'],
                'hidden_talents': ['Interior design', 'Counseling', 'Cooking', 'History and genealogy']
            },
            'Leo': {
                'overview': "You radiate warmth, creativity, and natural charisma. Ruled by the Sun, you possess an innate ability to light up any room and inspire others with your generous spirit.",
                'strengths': ['Creative', 'Passionate', 'Generous', 'Warm-hearted', 'Cheerful', 'Humorous'],
                'weaknesses': ['Arrogant', 'Stubborn', 'Self-centered', 'Inflexible', 'Dramatic'],
                'hidden_talents': ['Performing arts', 'Leadership roles', 'Event planning', 'Fashion and style']
            },
            'Virgo': {
                'overview': "Your analytical mind and attention to detail are unparalleled. Ruled by Mercury, you excel at organization and have a genuine desire to be of service to others.",
                'strengths': ['Analytical', 'Hardworking', 'Practical', 'Reliable', 'Precise', 'Helpful'],
                'weaknesses': ['Critical', 'Perfectionist', 'Overthinking', 'Worrisome', 'Self-critical'],
                'hidden_talents': ['Data analysis', 'Healthcare', 'Editing and proofreading', 'Nutrition and wellness']
            },
            'Libra': {
                'overview': "You are a natural diplomat with an innate sense of justice and harmony. Ruled by Venus, you appreciate beauty in all forms and strive to create balance in your life.",
                'strengths': ['Diplomatic', 'Fair-minded', 'Social', 'Cooperative', 'Gracious', 'Artistic'],
                'weaknesses': ['Indecisive', 'Avoids confrontation', 'Self-pitying', 'Can hold grudges'],
                'hidden_talents': ['Mediation and law', 'Art and design', 'Public relations', 'Matchmaking']
            },
            'Scorpio': {
                'overview': "You possess an intensity and depth that few can match. Ruled by Pluto, you have remarkable powers of transformation and an ability to see beyond surface appearances.",
                'strengths': ['Resourceful', 'Brave', 'Passionate', 'Determined', 'Honest', 'Strategic'],
                'weaknesses': ['Jealous', 'Secretive', 'Manipulative', 'Suspicious', 'Obsessive'],
                'hidden_talents': ['Investigation and research', 'Psychology', 'Finance', 'Healing arts']
            },
            'Sagittarius': {
                'overview': "Your spirit craves adventure, knowledge, and freedom. Ruled by Jupiter, you possess natural optimism and a philosophical outlook that seeks meaning in all experiences.",
                'strengths': ['Generous', 'Idealistic', 'Great sense of humor', 'Adventurous', 'Honest', 'Philosophical'],
                'weaknesses': ['Promises more than can deliver', 'Impatient', 'Tactless', 'Restless'],
                'hidden_talents': ['Travel and exploration', 'Teaching philosophy', 'Publishing', 'Athletics']
            },
            'Capricorn': {
                'overview': "You embody ambition, discipline, and practical wisdom. Ruled by Saturn, you understand that lasting success comes from patience, hard work, and strategic planning.",
                'strengths': ['Responsible', 'Disciplined', 'Self-control', 'Good managers', 'Ambitious', 'Practical'],
                'weaknesses': ['Know-it-all', 'Unforgiving', 'Condescending', 'Pessimistic', 'Workaholic'],
                'hidden_talents': ['Business management', 'Architecture', 'Politics', 'Long-term investing']
            },
            'Aquarius': {
                'overview': "You are a visionary thinker with humanitarian ideals. Ruled by Uranus, you march to the beat of your own drum and often see possibilities others miss.",
                'strengths': ['Progressive', 'Original', 'Independent', 'Humanitarian', 'Inventive', 'Intellectual'],
                'weaknesses': ['Emotionally detached', 'Temperamental', 'Uncompromising', 'Aloof'],
                'hidden_talents': ['Technology and innovation', 'Social activism', 'Scientific research', 'Astrology']
            },
            'Pisces': {
                'overview': "You possess a deeply intuitive and artistic soul. Ruled by Neptune, you navigate life with imagination, compassion, and a connection to the unseen realms.",
                'strengths': ['Compassionate', 'Artistic', 'Intuitive', 'Gentle', 'Wise', 'Musical'],
                'weaknesses': ['Fearful', 'Overly trusting', 'Escapist', 'Desire to escape reality', 'Melancholic'],
                'hidden_talents': ['Visual arts', 'Music and dance', 'Spiritual counseling', 'Film and photography']
            }
        }
        
        # Career suggestions by element
        self.career_suggestions = {
            'Fire': [
                'Entrepreneur or startup founder',
                'Sales and marketing executive',
                'Athletic coach or sports professional',
                'Emergency services (firefighter, paramedic)',
                'Military or law enforcement',
                'Motivational speaker or life coach'
            ],
            'Earth': [
                'Financial advisor or accountant',
                'Real estate developer or agent',
                'Agriculture or environmental science',
                'Architecture or construction management',
                'Healthcare administration',
                'Luxury goods or fine dining industry'
            ],
            'Air': [
                'Writer, journalist, or content creator',
                'Teacher or professor',
                'Technology and software development',
                'Public relations or communications',
                'Aviation industry',
                'Social media strategist'
            ],
            'Water': [
                'Counselor or therapist',
                'Healthcare professional (nursing, medicine)',
                'Artist or musician',
                'Marine biology or oceanography',
                'Hospitality and customer care',
                'Non-profit and charitable work'
            ]
        }
        
        # Motivational quotes for daily inspiration
        self.daily_quotes = [
            "The stars incline, but do not compel. You are the author of your destiny.",
            "Every sunrise brings new possibilities. Embrace today with open arms.",
            "Your potential is written in the cosmos, but unlocked by your actions.",
            "Trust the journey. The universe has a plan greater than you can imagine.",
            "In the dance of planets, you are both the dancer and the choreographer.",
            "Let your inner light shine as bright as the stars that guide you.",
            "The same energy that moves the galaxies flows through you.",
            "Today is a gift from the cosmos. Use it wisely and with gratitude.",
            "Your soul chose this moment to be here. Make it count.",
            "Like the moon, you may go through phases, but your light remains constant."
        ]
    
    def generate_full_report(self, user_data: dict, astrology_data: dict) -> dict:
        """
        Generate a comprehensive astrology report.
        
        Args:
            user_data: User's personal information
            astrology_data: Calculated astrological data
            
        Returns:
            Dictionary containing all report sections
        """
        zodiac = astrology_data['zodiac_sign']
        element = astrology_data['element']
        traits = self.personality_traits.get(zodiac, self.personality_traits['Aries'])
        
        # Build the complete report
        report = {
            # Personal Overview
            'personality_overview': traits['overview'],
            'strengths': traits['strengths'],
            'weaknesses': traits['weaknesses'],
            'hidden_talents': traits['hidden_talents'],
            
            # Career & Education
            'career_suggestions': self.career_suggestions.get(element, []),
            'education_guidance': self._generate_education_guidance(zodiac, element, user_data.get('education_level', '')),
            
            # Financial Outlook
            'financial_outlook': self._generate_financial_outlook(zodiac, element),
            
            # Relationships
            'relationship_insights': self._generate_relationship_insights(zodiac, user_data.get('relationship_status', '')),
            'marriage_compatibility': self._generate_compatibility(zodiac),
            'family_life': self._generate_family_insights(zodiac, element),
            
            # Health & Wellness
            'health_wellness': self._generate_health_tips(zodiac, element),
            
            # Travel
            'travel_opportunities': self._generate_travel_suggestions(element, astrology_data['lucky_direction']),
            
            # Horoscopes
            'monthly_horoscope': self._generate_monthly_horoscope(zodiac),
            'yearly_horoscope': self._generate_yearly_horoscope(zodiac, user_data),
            
            # Daily Inspiration
            'daily_quote': random.choice(self.daily_quotes),
            'motivational_advice': self._generate_motivational_advice(zodiac, user_data.get('occupation', '')),
            
            # Progress indicators (0-100 scale for visual display)
            'life_meters': {
                'career': self._calculate_meter(astrology_data, 'career'),
                'love': self._calculate_meter(astrology_data, 'love'),
                'health': self._calculate_meter(astrology_data, 'health'),
                'finance': self._calculate_meter(astrology_data, 'finance'),
                'happiness': self._calculate_meter(astrology_data, 'happiness')
            },
            
            # Disclaimer
            'disclaimer': "This astrology report is AI-generated for entertainment and self-reflection. It should not be considered factual or used as the sole basis for important life decisions."
        }
        
        return report
    
    def _generate_education_guidance(self, zodiac: str, element: str, education_level: str) -> str:
        """Generate personalized education guidance."""
        element_guidance = {
            'Fire': "Your energetic nature thrives in dynamic learning environments. Consider hands-on programs, competitive academic settings, or entrepreneurial courses. You learn best through action and experience.",
            'Earth': "You excel in structured, methodical learning. Practical certifications, professional degrees, and skill-based training align with your nature. Take your time to build a solid foundation.",
            'Air': "Your intellectual curiosity makes you a natural scholar. Liberal arts, communications, technology, and research fields suit you well. Seek programs that encourage discussion and diverse perspectives.",
            'Water': "You learn deeply through emotional connection to subjects. Arts, humanities, psychology, and healing fields resonate with you. Seek mentors who inspire and nurture your growth."
        }
        
        return element_guidance.get(element, "Pursue education that aligns with your passions and natural talents.")
    
    def _generate_financial_outlook(self, zodiac: str, element: str) -> str:
        """Generate financial insights based on astrological profile."""
        outlooks = {
            'Fire': "Your bold nature can lead to significant financial opportunities through entrepreneurship and calculated risks. However, practice patience with long-term investments. Your challenge is balancing impulse purchases with strategic saving.",
            'Earth': "Financial stability is your natural domain. You have an intuitive understanding of value and tend to build wealth steadily over time. Real estate and tangible assets particularly favor you. Trust your practical instincts.",
            'Air': "Your quick mind spots opportunities others miss. Technology investments and intellectual property may serve you well. Create systems to track finances, as details may sometimes escape you in pursuit of big ideas.",
            'Water': "Trust your intuition in financial matters—it's stronger than you realize. You may find success in creative industries or helping professions. Build an emergency fund to address the security your emotional nature needs."
        }
        
        return outlooks.get(element, "Balance intuition with research in all financial decisions.")
    
    def _generate_relationship_insights(self, zodiac: str, status: str) -> str:
        """Generate relationship insights based on zodiac and current status."""
        zodiac_love = {
            'Aries': "In love, you seek a partner who matches your energy and respects your independence. You're passionate and direct in expressing affection. The key to lasting love for you is finding someone who sees your vulnerability beneath the strong exterior.",
            'Taurus': "You offer deep loyalty and sensual romance to those you love. You seek security and consistency in relationships. The key for you is patience—you don't rush into love, but when you commit, it's for keeps.",
            'Gemini': "You need intellectual stimulation in relationships. Conversation and shared curiosity keep your heart engaged. The key for you is finding a partner who appreciates your dual nature and gives you space to explore.",
            'Cancer': "You love deeply and create nurturing bonds with those close to you. Emotional security is essential for you. The key is finding someone who values home and family as much as you do.",
            'Leo': "You bring warmth, generosity, and drama to romance. You need to feel admired and appreciated. The key for you is finding a partner who celebrates your light while also seeing your deeper need for genuine connection.",
            'Virgo': "You show love through acts of service and attention to your partner's needs. You may analyze relationships, but your devotion runs deep. The key is accepting imperfection—in yourself and others.",
            'Libra': "Partnership is central to your life—you truly flourish in committed relationships. You seek harmony and mutual respect. The key for you is maintaining your individual identity while creating beautiful union.",
            'Scorpio': "You love with intensity and total commitment. Trust is everything to you. The key is allowing yourself to be vulnerable and trusting that deep connection is worth the risk.",
            'Sagittarius': "You need freedom and adventure in relationships. A partner who travels through life with you—literally and philosophically—is ideal. The key is finding someone who shares your optimism and quest for meaning.",
            'Capricorn': "You approach love with the same dedication you bring to your ambitions. You may be reserved initially, but your commitment is unshakeable. The key is balancing work and relationship with equal attention.",
            'Aquarius': "You seek a partner who respects your individuality and shares your ideals. Mental connection often precedes emotional intimacy for you. The key is embracing emotional vulnerability alongside intellectual connection.",
            'Pisces': "You love unconditionally and often sense your partner's needs before they express them. Romance and fantasy play important roles for you. The key is choosing partners who appreciate your depth without taking advantage of your giving nature."
        }
        
        return zodiac_love.get(zodiac, "Your unique nature brings special gifts to relationships.")
    
    def _generate_compatibility(self, zodiac: str) -> dict:
        """Generate marriage/partnership compatibility information."""
        compatibility = {
            'Aries': {'best': ['Leo', 'Sagittarius', 'Gemini', 'Aquarius'], 'challenging': ['Cancer', 'Capricorn']},
            'Taurus': {'best': ['Virgo', 'Capricorn', 'Cancer', 'Pisces'], 'challenging': ['Leo', 'Aquarius']},
            'Gemini': {'best': ['Libra', 'Aquarius', 'Aries', 'Leo'], 'challenging': ['Virgo', 'Pisces']},
            'Cancer': {'best': ['Scorpio', 'Pisces', 'Taurus', 'Virgo'], 'challenging': ['Aries', 'Libra']},
            'Leo': {'best': ['Aries', 'Sagittarius', 'Gemini', 'Libra'], 'challenging': ['Taurus', 'Scorpio']},
            'Virgo': {'best': ['Taurus', 'Capricorn', 'Cancer', 'Scorpio'], 'challenging': ['Gemini', 'Sagittarius']},
            'Libra': {'best': ['Gemini', 'Aquarius', 'Leo', 'Sagittarius'], 'challenging': ['Cancer', 'Capricorn']},
            'Scorpio': {'best': ['Cancer', 'Pisces', 'Virgo', 'Capricorn'], 'challenging': ['Leo', 'Aquarius']},
            'Sagittarius': {'best': ['Aries', 'Leo', 'Libra', 'Aquarius'], 'challenging': ['Virgo', 'Pisces']},
            'Capricorn': {'best': ['Taurus', 'Virgo', 'Scorpio', 'Pisces'], 'challenging': ['Aries', 'Libra']},
            'Aquarius': {'best': ['Gemini', 'Libra', 'Aries', 'Sagittarius'], 'challenging': ['Taurus', 'Scorpio']},
            'Pisces': {'best': ['Cancer', 'Scorpio', 'Taurus', 'Capricorn'], 'challenging': ['Gemini', 'Sagittarius']}
        }
        
        data = compatibility.get(zodiac, {'best': [], 'challenging': []})
        return {
            'most_compatible': data['best'],
            'challenging_matches': data['challenging'],
            'note': "Compatibility is influenced by many factors beyond sun signs. These are traditional associations and should be taken as general guidance, not absolute rules."
        }
    
    def _generate_family_insights(self, zodiac: str, element: str) -> str:
        """Generate insights about family life."""
        insights = {
            'Fire': "You bring enthusiasm and adventure to family life. Your home is likely filled with activity and passion. As a parent or family member, you inspire others to pursue their dreams. Remember to balance excitement with moments of calm connection.",
            'Earth': "You provide stability and security for your family. Your home is likely comfortable and well-maintained. You show love through practical support and creating lasting traditions. Family meals and gatherings hold special meaning for you.",
            'Air': "You bring intellectual stimulation and open communication to family life. Your home encourages learning and diverse perspectives. You value teaching children to think independently and express themselves freely.",
            'Water': "Your family experiences deep emotional bonds under your care. You create a nurturing, intuitive home environment. You sense family members' needs and provide emotional support. Creating a sense of belonging is your gift."
        }
        
        return insights.get(element, "Your unique qualities enrich your family life in special ways.")
    
    def _generate_health_tips(self, zodiac: str, element: str) -> dict:
        """Generate health and wellness recommendations."""
        tips = {
            'Fire': {
                'focus_areas': ['Stress management', 'Heart health', 'Preventing burnout'],
                'recommended_activities': ['High-intensity interval training', 'Competitive sports', 'Dance', 'Hiking'],
                'wellness_tips': "Channel your abundant energy constructively. Include cooling practices like swimming. Watch for inflammation and practice relaxation techniques to balance your fiery nature."
            },
            'Earth': {
                'focus_areas': ['Digestive health', 'Weight management', 'Flexibility'],
                'recommended_activities': ['Yoga', 'Gardening', 'Walking in nature', 'Strength training'],
                'wellness_tips': "Your steady nature benefits from consistent routines. Focus on whole, natural foods. Movement is essential—combat tendencies toward sedentary habits with regular, enjoyable exercise."
            },
            'Air': {
                'focus_areas': ['Respiratory health', 'Nervous system', 'Mental wellness'],
                'recommended_activities': ['Breathwork', 'Tennis or racquet sports', 'Cycling', 'Group fitness'],
                'wellness_tips': "Mental stimulation is health for you—but so is mental rest. Practice breathing exercises and ensure quality sleep. Social exercise keeps you motivated and engaged."
            },
            'Water': {
                'focus_areas': ['Emotional wellness', 'Lymphatic system', 'Sleep quality'],
                'recommended_activities': ['Swimming', 'Tai Chi', 'Meditation', 'Gentle yoga'],
                'wellness_tips': "Your emotional and physical health are deeply connected. Water-based activities are naturally healing for you. Prioritize emotional processing and create boundaries to protect your sensitive nature."
            }
        }
        
        return tips.get(element, {'focus_areas': [], 'recommended_activities': [], 'wellness_tips': ""})
    
    def _generate_travel_suggestions(self, element: str, lucky_direction: str) -> dict:
        """Generate travel recommendations."""
        destinations = {
            'Fire': {
                'ideal_destinations': ['Spain', 'Morocco', 'Australia', 'Brazil', 'South Africa'],
                'travel_style': 'Adventure and active exploration',
                'tip': 'Seek destinations with warm climates, vibrant nightlife, and opportunities for adventure sports.'
            },
            'Earth': {
                'ideal_destinations': ['Italy', 'Japan', 'Switzerland', 'New Zealand', 'Scotland'],
                'travel_style': 'Cultural immersion and natural beauty',
                'tip': 'Luxury accommodations, wine regions, and destinations with rich history and stunning landscapes call to you.'
            },
            'Air': {
                'ideal_destinations': ['France', 'Netherlands', 'Singapore', 'Sweden', 'Canada'],
                'travel_style': 'Urban exploration and intellectual discovery',
                'tip': 'Cities with great museums, universities, and diverse populations stimulate your curious mind.'
            },
            'Water': {
                'ideal_destinations': ['Bali', 'Greece', 'Portugal', 'Thailand', 'Iceland'],
                'travel_style': 'Spiritual retreats and coastal escapes',
                'tip': 'Destinations near water, with spiritual significance or healing traditions, restore your soul.'
            }
        }
        
        travel_data = destinations.get(element, {})
        travel_data['lucky_direction'] = f"Consider traveling {lucky_direction} for enhanced luck and opportunity."
        
        return travel_data
    
    def _generate_monthly_horoscope(self, zodiac: str) -> str:
        """Generate a monthly horoscope interpretation."""
        # Using current month for personalization
        current_month = datetime.now().strftime('%B')
        
        horoscopes = {
            'Aries': f"{current_month} brings opportunities for bold action. Your leadership abilities are highlighted, and others look to you for direction. Mid-month may bring a financial opportunity worth exploring carefully.",
            'Taurus': f"This {current_month}, focus on building foundations. Property matters or home improvements are favored. Romance blossoms through shared activities. A creative project may yield unexpected results.",
            'Gemini': f"Communication is your superpower in {current_month}. Important conversations lead to breakthroughs. Short trips prove enlightening. A sibling or neighbor may play a significant role.",
            'Cancer': f"{current_month} emphasizes your emotional world. Family connections deepen. Trust your intuition in financial matters. Creating a peaceful home environment brings joy.",
            'Leo': f"Your star shines brightly in {current_month}. Creative projects flourish, and recognition comes your way. Romance is passionate. A child or creative venture may bring special joy.",
            'Virgo': f"{current_month} favors practical achievements. Your attention to detail solves problems others miss. Health routines established now have lasting benefits. A coworker becomes an ally.",
            'Libra': f"Relationships take center stage in {current_month}. Partnership decisions may arise. Artistic pursuits are favored. Social events bring valuable connections and possibly romance.",
            'Scorpio': f"Transformation continues through {current_month}. Release what no longer serves you. Deep research or investigation yields valuable insights. Intimate relationships intensify.",
            'Sagittarius': f"Adventure calls in {current_month}. Travel or educational pursuits are highly favored. Your optimism inspires others. Legal or publishing matters progress positively.",
            'Capricorn': f"{current_month} supports your ambitions. Career advancement is possible. Your reputation grows through dedicated work. An authority figure offers valuable guidance.",
            'Aquarius': f"Innovation is your theme for {current_month}. Technology and group activities are favored. Friendships bring unexpected opportunities. Your unique ideas gain acceptance.",
            'Pisces': f"Intuition is especially strong in {current_month}. Creative and spiritual pursuits flourish. Dreams may carry important messages. Compassionate actions return to you multiplied."
        }
        
        return horoscopes.get(zodiac, "This month holds unique opportunities aligned with your personal growth.")
    
    def _generate_yearly_horoscope(self, zodiac: str, user_data: dict) -> str:
        """Generate a yearly horoscope overview."""
        current_year = datetime.now().year
        
        # Generic but personalized yearly overview
        yearly_themes = {
            'Aries': f"In {current_year}, your pioneering spirit leads you to new territories. Career growth accelerates, especially in leadership roles. Relationships require patience and understanding.",
            'Taurus': f"{current_year} brings stability and growth to your foundations. Financial improvements are possible through steady effort. Love deepens when you open your heart.",
            'Gemini': f"Communication breakthroughs define your {current_year}. Learning and teaching opportunities abound. Travel expands your worldview. Siblings or neighbors play important roles.",
            'Cancer': f"Home and family are your focus in {current_year}. Property matters develop favorably. Emotional healing happens naturally. Career may shift toward more nurturing roles.",
            'Leo': f"{current_year} is your year to shine. Creative projects gain recognition. Romance is passionate and transformative. Children or creative ventures bring joy.",
            'Virgo': f"Health and service themes dominate your {current_year}. Work projects reach completion. Daily routines improve your wellbeing. A pet or small animal may bring comfort.",
            'Libra': f"Relationships transform in {current_year}. Partnerships—business and personal—require balance. Legal matters favor you. Artistic talents develop beautifully.",
            'Scorpio': f"{current_year} brings profound transformation. Release and renewal are your themes. Joint finances require attention. Intimacy deepens with trust.",
            'Sagittarius': f"Expansion defines your {current_year}. Higher education, travel, or publishing opportunities arise. Philosophical understanding deepens. Legal matters favor you.",
            'Capricorn': f"Career achievements highlight your {current_year}. Your reputation grows through dedication. Authority and responsibility increase. Family traditions anchor you.",
            'Aquarius': f"Innovation and community are your {current_year} themes. Technology brings opportunities. Friendships evolve significantly. Humanitarian causes call to you.",
            'Pisces': f"Spiritual growth marks your {current_year}. Intuition strengthens remarkably. Creative and artistic pursuits flourish. Hidden talents emerge into the light."
        }
        
        return yearly_themes.get(zodiac, f"{current_year} holds transformative potential for your unique path.")
    
    def _generate_motivational_advice(self, zodiac: str, occupation: str) -> str:
        """Generate personalized motivational advice."""
        base_advice = {
            'Aries': "Your courage is your compass. Trust your instincts and take bold action, but remember that true strength includes patience.",
            'Taurus': "Your persistence moves mountains. Trust in your steady progress and know that the foundations you build today support tomorrow's success.",
            'Gemini': "Your versatility is your greatest asset. Embrace your many interests while developing depth in what truly matters to you.",
            'Cancer': "Your sensitivity is a superpower. Use your emotional intelligence to nurture not only others but also your own dreams.",
            'Leo': "Your light inspires others. Lead with generosity and authenticity, and the recognition you deserve will naturally follow.",
            'Virgo': "Your attention to detail creates excellence. Trust that your careful work matters, and don't forget to appreciate your own achievements.",
            'Libra': "Your sense of harmony brings peace to chaos. Trust your diplomatic instincts while also honoring your own needs and boundaries.",
            'Scorpio': "Your depth and determination are unmatched. Use your transformative power to create positive change in yourself and the world.",
            'Sagittarius': "Your optimism opens doors. Keep exploring, learning, and sharing your wisdom—the journey itself is the destination.",
            'Capricorn': "Your discipline builds empires. Trust in your strategic mind, and remember to celebrate milestones along your steady climb.",
            'Aquarius': "Your vision sees the future. Trust your innovative ideas and remember that even revolutionaries need community.",
            'Pisces': "Your imagination creates worlds. Trust your intuition, protect your energy, and let your creativity flow without judgment."
        }
        
        return base_advice.get(zodiac, "Trust in your unique path. The universe has positioned you exactly where you need to be for your growth.")
    
    def _calculate_meter(self, astrology_data: dict, category: str) -> int:
        """
        Calculate a visual meter value (0-100) for life categories.
        Uses birth data to create consistent, personalized values.
        """
        # Use lucky number and life path as seeds for variation
        lucky = astrology_data.get('lucky_number', 5)
        life_path = astrology_data.get('life_path_number', 5)
        
        # Base calculation with category variation
        category_offsets = {
            'career': 10,
            'love': 20,
            'health': 30,
            'finance': 40,
            'happiness': 50
        }
        
        offset = category_offsets.get(category, 0)
        
        # Generate a value between 60-95 for positive presentation
        base = 60 + ((lucky * life_path + offset) % 36)
        
        return min(95, max(60, base))
