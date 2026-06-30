/**
 * Celestial Insights - AI Astrology Application
 * Main JavaScript Application File
 * =============================================
 * 
 * This file handles all client-side functionality including:
 * - Star animation background
 * - Form submission and validation
 * - Loading animation orchestration
 * - Report rendering with progressive reveal
 * - PDF download functionality
 */

// ============================================
// Application State
// ============================================

/**
 * Global application state object
 * Stores report data for PDF generation and other cross-function access
 */
const AppState = {
    reportData: null,
    isLoading: false
};

// ============================================
// Initialization
// ============================================

/**
 * Initialize the application when DOM is fully loaded
 */
document.addEventListener('DOMContentLoaded', () => {
    console.log('Celestial Insights Application Initialized');
    
    // Generate animated star background
    createStarField();
    
    // Set up form handling if on home page
    const form = document.getElementById('astrology-form');
    if (form) {
        form.addEventListener('submit', handleFormSubmit);
    }
    
    // Set up report page handlers if on report page
    const reportContainer = document.getElementById('report-container');
    if (reportContainer) {
        initializeReportPage();
    }
});

// ============================================
// Star Field Animation
// ============================================

/**
 * Creates an animated star field background
 * Generates random stars with varying sizes and twinkle animations
 */
function createStarField() {
    const container = document.getElementById('stars');
    if (!container) return;
    
    // Number of stars to generate
    const starCount = 150;
    
    // Clear any existing stars
    container.innerHTML = '';
    
    // Create each star
    for (let i = 0; i < starCount; i++) {
        const star = document.createElement('div');
        star.className = 'star';
        
        // Random position
        star.style.left = `${Math.random() * 100}%`;
        star.style.top = `${Math.random() * 100}%`;
        
        // Random animation duration and delay for natural twinkling
        const duration = 2 + Math.random() * 4; // 2-6 seconds
        const delay = Math.random() * 5; // 0-5 seconds delay
        star.style.setProperty('--duration', `${duration}s`);
        star.style.setProperty('--delay', `${delay}s`);
        
        // Some stars are larger
        if (Math.random() > 0.9) {
            star.classList.add('large');
        }
        
        container.appendChild(star);
    }
}

// ============================================
// Form Handling
// ============================================

/**
 * Handles the astrology form submission
 * @param {Event} event - The form submit event
 */
async function handleFormSubmit(event) {
    event.preventDefault();
    
    // Prevent double submission
    if (AppState.isLoading) return;
    
    // Show loading overlay
    showLoadingOverlay();
    
    // Collect form data
    const formData = new FormData(event.target);
    
    try {
        // Submit to server
        const response = await fetch('/generate-report', {
            method: 'POST',
            body: formData
        });
        
        if (!response.ok) {
            throw new Error('Failed to generate report');
        }
        
        const data = await response.json();
        
        if (!data.success) {
            throw new Error(data.error || 'Unknown error occurred');
        }
        
        // Store report data in sessionStorage for the report page
        sessionStorage.setItem('reportData', JSON.stringify(data));
        
        // Navigate to report page
        window.location.href = '/report';
        
    } catch (error) {
        console.error('Error generating report:', error);
        hideLoadingOverlay();
        alert('An error occurred while generating your report. Please try again.');
    }
}

// ============================================
// Loading Overlay
// ============================================

/**
 * Shows the loading overlay with animated messages
 */
function showLoadingOverlay() {
    const overlay = document.getElementById('loading-overlay');
    if (!overlay) return;
    
    AppState.isLoading = true;
    overlay.classList.add('active');
    
    // Cycle through loading messages
    cycleLoadingMessages();
}

/**
 * Hides the loading overlay
 */
function hideLoadingOverlay() {
    const overlay = document.getElementById('loading-overlay');
    if (!overlay) return;
    
    AppState.isLoading = false;
    overlay.classList.remove('active');
}

/**
 * Cycles through the loading messages with timing
 */
function cycleLoadingMessages() {
    const messages = [
        document.getElementById('message-1'),
        document.getElementById('message-2'),
        document.getElementById('message-3')
    ];
    
    if (!messages[0]) return;
    
    let currentIndex = 0;
    
    const cycleInterval = setInterval(() => {
        if (!AppState.isLoading) {
            clearInterval(cycleInterval);
            return;
        }
        
        // Remove active class from all messages
        messages.forEach(msg => msg?.classList.remove('active'));
        
        // Move to next message
        currentIndex = (currentIndex + 1) % messages.length;
        
        // Add active class to current message
        messages[currentIndex]?.classList.add('active');
        
    }, 2000); // Change message every 2 seconds
}

// ============================================
// Report Page
// ============================================

/**
 * Initializes the report page
 * Loads data from sessionStorage and renders the report
 */
function initializeReportPage() {
    // Check for stored report data
    const storedData = sessionStorage.getItem('reportData');
    
    if (!storedData) {
        // No data found, redirect to home
        window.location.href = '/';
        return;
    }
    
    try {
        const data = JSON.parse(storedData);
        AppState.reportData = data;
        
        // Hide loading, render report
        document.getElementById('report-loading')?.classList.add('hidden');
        renderReport(data);
        
    } catch (error) {
        console.error('Error parsing report data:', error);
        window.location.href = '/';
    }
}

/**
 * Renders the complete report with progressive reveal animation
 * @param {Object} data - The report data object
 */
function renderReport(data) {
    const { user_data, astrology_data, report } = data;
    
    // Array of sections to reveal in order
    const sections = [
        { id: 'report-header', delay: 0 },
        { id: 'zodiac-section', delay: 200 },
        { id: 'meters-section', delay: 400 },
        { id: 'personality-section', delay: 600 },
        { id: 'traits-section', delay: 800 },
        { id: 'talents-section', delay: 1000 },
        { id: 'career-section', delay: 1200 },
        { id: 'finance-section', delay: 1400 },
        { id: 'relationship-section', delay: 1600 },
        { id: 'health-section', delay: 1800 },
        { id: 'travel-section', delay: 2000 },
        { id: 'horoscope-section', delay: 2200 },
        { id: 'inspiration-section', delay: 2400 },
        { id: 'action-buttons', delay: 2600 },
        { id: 'report-disclaimer', delay: 2800 }
    ];
    
    // Populate data first
    populateReportData(user_data, astrology_data, report);
    
    // Reveal sections progressively
    sections.forEach(({ id, delay }) => {
        setTimeout(() => {
            const element = document.getElementById(id);
            if (element) {
                element.classList.remove('hidden');
            }
        }, delay);
    });
    
    // Animate meters after they become visible
    setTimeout(() => {
        animateMeters(report.life_meters);
    }, 600);
    
    // Set up event handlers
    setupReportEventHandlers();
}

/**
 * Populates all report data into the DOM
 * @param {Object} userData - User's personal information
 * @param {Object} astrologyData - Calculated astrology data
 * @param {Object} report - Generated report content
 */
function populateReportData(userData, astrologyData, report) {
    // Header
    setText('report-name', `Prepared for ${userData.full_name}`);
    setText('report-date', `Generated on ${new Date().toLocaleDateString('en-US', { 
        weekday: 'long', 
        year: 'numeric', 
        month: 'long', 
        day: 'numeric' 
    })}`);
    
    // Zodiac Profile
    setText('zodiac-symbol', astrologyData.zodiac_symbol);
    setText('zodiac-name', astrologyData.zodiac_sign);
    setText('zodiac-element', `${astrologyData.element} Element`);
    setText('chinese-zodiac', `${astrologyData.chinese_zodiac} ${astrologyData.chinese_symbol}`);
    setText('lucky-number', astrologyData.lucky_number);
    setText('lucky-color', astrologyData.lucky_color);
    setText('lucky-day', astrologyData.lucky_day);
    setText('lucky-gemstone', astrologyData.lucky_gemstone);
    setText('lucky-direction', astrologyData.lucky_direction);
    
    // Personality
    setText('personality-overview', report.personality_overview);
    
    // Strengths & Weaknesses
    renderList('strengths-list', report.strengths);
    renderList('weaknesses-list', report.weaknesses);
    
    // Hidden Talents
    renderTalents('talents-grid', report.hidden_talents);
    
    // Career
    renderCareers('career-grid', report.career_suggestions);
    setText('education-guidance', report.education_guidance);
    
    // Finance
    setText('financial-outlook', report.financial_outlook);
    
    // Relationships
    setText('relationship-insights', report.relationship_insights);
    renderSignBadges('compatible-signs', report.marriage_compatibility.most_compatible);
    renderSignBadges('challenging-signs', report.marriage_compatibility.challenging_matches, true);
    setText('family-life', report.family_life);
    
    // Health
    renderList('health-focus-list', report.health_wellness.focus_areas);
    renderList('health-activities-list', report.health_wellness.recommended_activities);
    setText('wellness-tips', report.health_wellness.wellness_tips);
    
    // Travel
    setText('travel-style', report.travel_opportunities.travel_style);
    setText('travel-direction', report.travel_opportunities.lucky_direction);
    renderDestinations('destinations-grid', report.travel_opportunities.ideal_destinations);
    setText('travel-tip', report.travel_opportunities.tip);
    
    // Horoscopes
    setText('monthly-horoscope', report.monthly_horoscope);
    setText('yearly-horoscope', report.yearly_horoscope);
    
    // Inspiration
    setText('daily-quote', report.daily_quote);
    setText('motivational-advice', report.motivational_advice);
    
    // Disclaimer
    setText('disclaimer-text', report.disclaimer);
}

/**
 * Sets text content of an element by ID
 * @param {string} id - Element ID
 * @param {string} text - Text to set
 */
function setText(id, text) {
    const element = document.getElementById(id);
    if (element) {
        element.textContent = text;
    }
}

/**
 * Renders a list of items into a UL element
 * @param {string} id - UL element ID
 * @param {Array} items - Array of items to render
 */
function renderList(id, items) {
    const element = document.getElementById(id);
    if (!element || !Array.isArray(items)) return;
    
    element.innerHTML = items.map(item => `<li>${item}</li>`).join('');
}

/**
 * Renders talent badges
 * @param {string} id - Container element ID
 * @param {Array} talents - Array of talents
 */
function renderTalents(id, talents) {
    const element = document.getElementById(id);
    if (!element || !Array.isArray(talents)) return;
    
    element.innerHTML = talents.map(talent => 
        `<span class="talent-item">${talent}</span>`
    ).join('');
}

/**
 * Renders career suggestion cards
 * @param {string} id - Container element ID
 * @param {Array} careers - Array of career suggestions
 */
function renderCareers(id, careers) {
    const element = document.getElementById(id);
    if (!element || !Array.isArray(careers)) return;
    
    element.innerHTML = careers.slice(0, 6).map(career => 
        `<div class="career-item">${career}</div>`
    ).join('');
}

/**
 * Renders zodiac sign badges
 * @param {string} id - Container element ID
 * @param {Array} signs - Array of zodiac signs
 * @param {boolean} challenging - Whether these are challenging matches
 */
function renderSignBadges(id, signs, challenging = false) {
    const element = document.getElementById(id);
    if (!element || !Array.isArray(signs)) return;
    
    element.innerHTML = signs.map(sign => 
        `<span class="sign-badge">${sign}</span>`
    ).join('');
}

/**
 * Renders destination badges
 * @param {string} id - Container element ID
 * @param {Array} destinations - Array of destinations
 */
function renderDestinations(id, destinations) {
    const element = document.getElementById(id);
    if (!element || !Array.isArray(destinations)) return;
    
    element.innerHTML = destinations.map(dest => 
        `<span class="destination-badge">${dest}</span>`
    ).join('');
}

/**
 * Animates the life meter progress bars
 * @param {Object} meters - Object containing meter values
 */
function animateMeters(meters) {
    if (!meters) return;
    
    const meterTypes = ['career', 'love', 'health', 'finance', 'happiness'];
    
    meterTypes.forEach((type, index) => {
        setTimeout(() => {
            const fill = document.getElementById(`meter-${type}`);
            const value = document.getElementById(`meter-${type}-value`);
            const percentage = meters[type] || 0;
            
            if (fill) {
                fill.style.width = `${percentage}%`;
            }
            if (value) {
                // Animate the number counting up
                animateCounter(value, 0, percentage, 1000);
            }
        }, index * 200); // Stagger each meter animation
    });
}

/**
 * Animates a number counter
 * @param {Element} element - Element to update
 * @param {number} start - Starting value
 * @param {number} end - Ending value
 * @param {number} duration - Animation duration in ms
 */
function animateCounter(element, start, end, duration) {
    const startTime = performance.now();
    
    function update(currentTime) {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        
        // Easing function (ease-out)
        const easeOut = 1 - Math.pow(1 - progress, 3);
        const current = Math.round(start + (end - start) * easeOut);
        
        element.textContent = `${current}%`;
        
        if (progress < 1) {
            requestAnimationFrame(update);
        }
    }
    
    requestAnimationFrame(update);
}

/**
 * Sets up event handlers for the report page
 */
function setupReportEventHandlers() {
    // Horoscope tabs
    const tabBtns = document.querySelectorAll('.tab-btn');
    tabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            // Remove active from all tabs and contents
            tabBtns.forEach(b => b.classList.remove('active'));
            document.querySelectorAll('.tab-content').forEach(c => c.classList.remove('active'));
            
            // Add active to clicked tab
            btn.classList.add('active');
            
            // Show corresponding content
            const tabId = btn.dataset.tab;
            document.getElementById(`${tabId}-horoscope`)?.classList.add('active');
        });
    });
    
    // Download PDF button
    const downloadBtn = document.getElementById('download-pdf');
    if (downloadBtn) {
        downloadBtn.addEventListener('click', handlePdfDownload);
    }
    
    // New Reading button
    const newReadingBtn = document.getElementById('new-reading');
    if (newReadingBtn) {
        newReadingBtn.addEventListener('click', () => {
            // Clear stored data and go to home
            sessionStorage.removeItem('reportData');
            window.location.href = '/';
        });
    }
}

/**
 * Handles PDF download request
 */
async function handlePdfDownload() {
    if (!AppState.reportData) {
        alert('No report data available');
        return;
    }
    
    const downloadBtn = document.getElementById('download-pdf');
    const originalText = downloadBtn.innerHTML;
    
    try {
        // Update button state
        downloadBtn.innerHTML = '<span class="btn-icon">⏳</span><span>Generating PDF...</span>';
        downloadBtn.disabled = true;
        
        // Request PDF from server
        const response = await fetch('/download-pdf', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(AppState.reportData)
        });
        
        if (!response.ok) {
            throw new Error('Failed to generate PDF');
        }
        
        // Create download link
        const blob = await response.blob();
        const url = window.URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `astrology_report_${new Date().toISOString().split('T')[0]}.pdf`;
        document.body.appendChild(a);
        a.click();
        
        // Cleanup
        window.URL.revokeObjectURL(url);
        document.body.removeChild(a);
        
    } catch (error) {
        console.error('Error downloading PDF:', error);
        alert('Failed to download PDF. Please try again.');
        
    } finally {
        // Restore button
        downloadBtn.innerHTML = originalText;
        downloadBtn.disabled = false;
    }
}
