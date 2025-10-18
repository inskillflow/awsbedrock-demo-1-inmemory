// Application JavaScript pour la gestion des employés

class EmployeeManager {
    constructor() {
        this.employees = [];
        this.skills = [];
        this.filteredEmployees = [];
        this.currentEmployeeId = null;
        this.init();
    }

    async init() {
        this.setupEventListeners();
        await this.loadData();
        this.renderEmployees();
        this.setupFilters();
    }

    setupEventListeners() {
        // Tab navigation
        document.querySelectorAll('.tab-btn').forEach(btn => {
            btn.addEventListener('click', (e) => this.switchTab(e.target.dataset.tab));
        });

        // Modal controls
        document.getElementById('addEmployeeBtn').addEventListener('click', () => this.openModal());
        document.getElementById('closeModal').addEventListener('click', () => this.closeModal());
        document.getElementById('cancelBtn').addEventListener('click', () => this.closeModal());
        document.getElementById('employeeForm').addEventListener('submit', (e) => this.handleFormSubmit(e));

        // Filters
        document.getElementById('searchInput').addEventListener('input', () => this.applyFilters());
        document.getElementById('departmentFilter').addEventListener('change', () => this.applyFilters());
        document.getElementById('skillFilter').addEventListener('change', () => this.applyFilters());

        // Close modal on outside click
        document.getElementById('employeeModal').addEventListener('click', (e) => {
            if (e.target.id === 'employeeModal') this.closeModal();
        });

        // Chat event listeners
        document.getElementById('chatForm').addEventListener('submit', (e) => this.handleChatSubmit(e));
        
        // Quick questions
        document.querySelectorAll('.quick-question').forEach(btn => {
            btn.addEventListener('click', (e) => {
                const question = e.currentTarget.dataset.question;
                this.askQuestion(question);
            });
        });
    }

    async loadData() {
        try {
            const [employeesResponse, skillsResponse] = await Promise.all([
                axios.get('/api/employees'),
                axios.get('/api/skills')
            ]);
            
            this.employees = employeesResponse.data;
            this.skills = skillsResponse.data;
            this.filteredEmployees = [...this.employees];
        } catch (error) {
            console.error('Erreur lors du chargement des données:', error);
            this.showNotification('Erreur lors du chargement des données', 'error');
        }
    }

    switchTab(tabName) {
        // Update tab buttons
        document.querySelectorAll('.tab-btn').forEach(btn => {
            btn.classList.remove('active', 'text-blue-600', 'border-blue-500');
            btn.classList.add('border-transparent');
        });
        
        const activeTab = document.querySelector(`[data-tab="${tabName}"]`);
        activeTab.classList.add('active', 'text-blue-600', 'border-blue-500');
        activeTab.classList.remove('border-transparent');

        // Show/hide content
        document.querySelectorAll('.tab-content').forEach(content => {
            content.classList.add('hidden');
        });
        document.getElementById(`${tabName}-tab`).classList.remove('hidden');

        // Load specific content
        switch(tabName) {
            case 'skills':
                this.renderSkills();
                break;
            case 'stats':
                this.loadStats();
                break;
            case 'chat':
                this.initChat();
                break;
        }
    }

    renderEmployees() {
        const grid = document.getElementById('employeesGrid');
        grid.innerHTML = '';

        this.filteredEmployees.forEach(employee => {
            const card = this.createEmployeeCard(employee);
            grid.appendChild(card);
        });
    }

    createEmployeeCard(employee) {
        const div = document.createElement('div');
        div.className = 'bg-white rounded-lg shadow-md p-6 hover:shadow-lg transition-shadow';
        
        const skillsBadges = employee.skills.map(skill => 
            `<span class="inline-block bg-blue-100 text-blue-800 text-xs px-2 py-1 rounded-full mr-1 mb-1">${skill}</span>`
        ).join('');

        div.innerHTML = `
            <div class="flex justify-between items-start mb-4">
                <div>
                    <h3 class="text-lg font-semibold text-gray-900">${employee.name}</h3>
                    <p class="text-sm text-gray-600">${employee.position}</p>
                    <p class="text-sm text-gray-500">${employee.department}</p>
                </div>
                <div class="flex space-x-2">
                    <button onclick="employeeManager.editEmployee(${employee.id})" 
                            class="text-blue-600 hover:text-blue-800">
                        <i class="fas fa-edit"></i>
                    </button>
                    <button onclick="employeeManager.deleteEmployee(${employee.id})" 
                            class="text-red-600 hover:text-red-800">
                        <i class="fas fa-trash"></i>
                    </button>
                </div>
            </div>
            
            <div class="mb-3">
                <p class="text-sm text-gray-600">
                    <i class="fas fa-envelope mr-1"></i>${employee.email}
                </p>
                <p class="text-sm text-gray-600">
                    <i class="fas fa-calendar mr-1"></i>${employee.experience_years} ans d'expérience
                </p>
                <p class="text-sm text-gray-600">
                    <i class="fas fa-euro-sign mr-1"></i>${employee.salary.toLocaleString()}€
                </p>
            </div>
            
            <div class="mb-3">
                <p class="text-sm font-medium text-gray-700 mb-2">Compétences:</p>
                <div class="flex flex-wrap">
                    ${skillsBadges}
                </div>
            </div>
        `;

        return div;
    }

    setupFilters() {
        // Setup department filter
        const departments = [...new Set(this.employees.map(emp => emp.department))];
        const departmentFilter = document.getElementById('departmentFilter');
        departments.forEach(dept => {
            const option = document.createElement('option');
            option.value = dept;
            option.textContent = dept;
            departmentFilter.appendChild(option);
        });

        // Setup skill filter
        const skillFilter = document.getElementById('skillFilter');
        this.skills.forEach(skill => {
            const option = document.createElement('option');
            option.value = skill;
            option.textContent = skill;
            skillFilter.appendChild(option);
        });
    }

    applyFilters() {
        const searchTerm = document.getElementById('searchInput').value.toLowerCase();
        const departmentFilter = document.getElementById('departmentFilter').value;
        const skillFilter = document.getElementById('skillFilter').value;

        this.filteredEmployees = this.employees.filter(employee => {
            const matchesSearch = searchTerm === '' || 
                employee.name.toLowerCase().includes(searchTerm) ||
                employee.email.toLowerCase().includes(searchTerm) ||
                employee.position.toLowerCase().includes(searchTerm);

            const matchesDepartment = departmentFilter === '' || 
                employee.department === departmentFilter;

            const matchesSkill = skillFilter === '' || 
                employee.skills.includes(skillFilter);

            return matchesSearch && matchesDepartment && matchesSkill;
        });

        this.renderEmployees();
    }

    renderSkills() {
        const skillsList = document.getElementById('skillsList');
        skillsList.innerHTML = '';

        this.skills.forEach(skill => {
            const count = this.employees.reduce((acc, emp) => 
                acc + (emp.skills.includes(skill) ? 1 : 0), 0);
            
            const div = document.createElement('div');
            div.className = 'bg-blue-50 border border-blue-200 rounded-lg p-3 text-center';
            div.innerHTML = `
                <div class="font-medium text-blue-900">${skill}</div>
                <div class="text-sm text-blue-600">${count} employé${count !== 1 ? 's' : ''}</div>
            `;
            skillsList.appendChild(div);
        });
    }

    async loadStats() {
        try {
            const response = await axios.get('/api/stats');
            const stats = response.data;

            // Update summary cards
            document.getElementById('totalEmployees').textContent = stats.total_employees;
            document.getElementById('avgSalary').textContent = Math.round(stats.average_salary).toLocaleString() + '€';
            document.getElementById('totalSkills').textContent = stats.total_skills;
            document.getElementById('totalDepartments').textContent = Object.keys(stats.departments).length;

            // Render department stats
            this.renderDepartmentStats(stats.departments);
            this.renderSkillsStats(stats.skills_distribution);
        } catch (error) {
            console.error('Erreur lors du chargement des statistiques:', error);
        }
    }

    renderDepartmentStats(departments) {
        const container = document.getElementById('departmentStats');
        container.innerHTML = '';

        Object.entries(departments).forEach(([dept, data]) => {
            const div = document.createElement('div');
            div.className = 'flex justify-between items-center py-2 border-b border-gray-200';
            div.innerHTML = `
                <div>
                    <div class="font-medium">${dept}</div>
                    <div class="text-sm text-gray-600">${data.count} employé${data.count !== 1 ? 's' : ''}</div>
                </div>
                <div class="text-right">
                    <div class="font-medium">${Math.round(data.avg_salary).toLocaleString()}€</div>
                    <div class="text-sm text-gray-600">Salaire moyen</div>
                </div>
            `;
            container.appendChild(div);
        });
    }

    renderSkillsStats(skillsDistribution) {
        const container = document.getElementById('skillsStats');
        container.innerHTML = '';

        // Sort skills by count and take top 10
        const sortedSkills = Object.entries(skillsDistribution)
            .sort(([,a], [,b]) => b - a)
            .slice(0, 10);

        sortedSkills.forEach(([skill, count]) => {
            const maxCount = Math.max(...Object.values(skillsDistribution));
            const percentage = (count / maxCount) * 100;
            
            const div = document.createElement('div');
            div.className = 'mb-2';
            div.innerHTML = `
                <div class="flex justify-between text-sm mb-1">
                    <span>${skill}</span>
                    <span>${count}</span>
                </div>
                <div class="w-full bg-gray-200 rounded-full h-2">
                    <div class="bg-blue-600 h-2 rounded-full" style="width: ${percentage}%"></div>
                </div>
            `;
            container.appendChild(div);
        });
    }

    openModal(employee = null) {
        this.currentEmployeeId = employee ? employee.id : null;
        const modal = document.getElementById('employeeModal');
        const title = document.getElementById('modalTitle');
        
        title.textContent = employee ? 'Modifier l\'Employé' : 'Ajouter un Employé';
        
        // Setup skills checkboxes
        this.setupSkillsCheckboxes();
        
        if (employee) {
            this.populateForm(employee);
        } else {
            this.clearForm();
        }
        
        modal.classList.remove('hidden');
    }

    closeModal() {
        document.getElementById('employeeModal').classList.add('hidden');
        this.clearForm();
        this.currentEmployeeId = null;
    }

    setupSkillsCheckboxes() {
        const container = document.getElementById('skillsCheckboxes');
        container.innerHTML = '';

        this.skills.forEach(skill => {
            const div = document.createElement('div');
            div.className = 'flex items-center space-x-2 mb-1';
            div.innerHTML = `
                <input type="checkbox" id="skill-${skill}" value="${skill}" 
                       class="text-blue-600 focus:ring-blue-500">
                <label for="skill-${skill}" class="text-sm">${skill}</label>
            `;
            container.appendChild(div);
        });
    }

    populateForm(employee) {
        document.getElementById('employeeName').value = employee.name;
        document.getElementById('employeeEmail').value = employee.email;
        document.getElementById('employeeDepartment').value = employee.department;
        document.getElementById('employeePosition').value = employee.position;
        document.getElementById('employeeExperience').value = employee.experience_years;
        document.getElementById('employeeSalary').value = employee.salary;

        // Check relevant skills
        employee.skills.forEach(skill => {
            const checkbox = document.getElementById(`skill-${skill}`);
            if (checkbox) checkbox.checked = true;
        });
    }

    clearForm() {
        document.getElementById('employeeForm').reset();
        document.querySelectorAll('#skillsCheckboxes input[type="checkbox"]').forEach(cb => {
            cb.checked = false;
        });
    }

    async handleFormSubmit(e) {
        e.preventDefault();
        
        const formData = {
            name: document.getElementById('employeeName').value,
            email: document.getElementById('employeeEmail').value,
            department: document.getElementById('employeeDepartment').value,
            position: document.getElementById('employeePosition').value,
            experience_years: parseInt(document.getElementById('employeeExperience').value),
            salary: parseFloat(document.getElementById('employeeSalary').value),
            skills: Array.from(document.querySelectorAll('#skillsCheckboxes input[type="checkbox"]:checked'))
                       .map(cb => cb.value)
        };

        try {
            if (this.currentEmployeeId) {
                await axios.put(`/api/employees/${this.currentEmployeeId}`, formData);
                this.showNotification('Employé modifié avec succès', 'success');
            } else {
                await axios.post('/api/employees', formData);
                this.showNotification('Employé ajouté avec succès', 'success');
            }
            
            await this.loadData();
            this.renderEmployees();
            this.setupFilters();
            this.closeModal();
        } catch (error) {
            console.error('Erreur lors de la sauvegarde:', error);
            this.showNotification('Erreur lors de la sauvegarde', 'error');
        }
    }

    async editEmployee(id) {
        const employee = this.employees.find(emp => emp.id === id);
        if (employee) {
            this.openModal(employee);
        }
    }

    async deleteEmployee(id) {
        if (!confirm('Êtes-vous sûr de vouloir supprimer cet employé ?')) {
            return;
        }

        try {
            await axios.delete(`/api/employees/${id}`);
            this.showNotification('Employé supprimé avec succès', 'success');
            await this.loadData();
            this.renderEmployees();
            this.setupFilters();
        } catch (error) {
            console.error('Erreur lors de la suppression:', error);
            this.showNotification('Erreur lors de la suppression', 'error');
        }
    }

    showNotification(message, type = 'info') {
        // Simple notification system
        const notification = document.createElement('div');
        notification.className = `fixed top-4 right-4 p-4 rounded-lg shadow-lg z-50 ${
            type === 'success' ? 'bg-green-500 text-white' :
            type === 'error' ? 'bg-red-500 text-white' :
            'bg-blue-500 text-white'
        }`;
        notification.textContent = message;
        
        document.body.appendChild(notification);
        
        setTimeout(() => {
            notification.remove();
        }, 3000);
    }

    // Chat functionality
    async initChat() {
        await this.loadChatStats();
        await this.checkAgentHealth();
    }

    async loadChatStats() {
        const departments = [...new Set(this.employees.map(emp => emp.department))];
        document.getElementById('chatEmployeeCount').textContent = this.employees.length;
        document.getElementById('chatSkillCount').textContent = this.skills.length;
        document.getElementById('chatDeptCount').textContent = departments.length;
    }

    async checkAgentHealth() {
        try {
            const response = await axios.get('/api/agent/health');
            const health = response.data;
            
            const statusElement = document.getElementById('agentStatus');
            if (health.agent_status === 'healthy') {
                statusElement.textContent = health.bedrock_available ? 'AI' : 'OK';
                statusElement.title = health.bedrock_available ? 'AWS Bedrock' : 'Mode Local';
            } else {
                statusElement.textContent = 'ERR';
                statusElement.title = 'Agent indisponible';
            }
        } catch (error) {
            console.error('Erreur lors de la vérification de l\'agent:', error);
            document.getElementById('agentStatus').textContent = 'ERR';
        }
    }

    async handleChatSubmit(e) {
        e.preventDefault();
        const input = document.getElementById('chatInput');
        const question = input.value.trim();
        
        if (!question) return;
        
        input.value = '';
        await this.askQuestion(question);
    }

    async askQuestion(question) {
        const chatMessages = document.getElementById('chatMessages');
        const sendBtn = document.getElementById('chatSendBtn');
        
        // Disable send button
        sendBtn.disabled = true;
        sendBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i>';
        
        // Add user message
        this.addChatMessage(question, 'user');
        
        try {
            const response = await axios.post('/api/inquire', { question });
            const aiResponse = response.data;
            
            // Add AI response
            this.addChatMessage(aiResponse.answer, 'ai', aiResponse.model);
            
        } catch (error) {
            console.error('Erreur lors de la question:', error);
            this.addChatMessage('Désolé, je n\'ai pas pu traiter votre question. Veuillez réessayer.', 'ai', 'Erreur');
        }
        
        // Re-enable send button
        sendBtn.disabled = false;
        sendBtn.innerHTML = '<i class="fas fa-paper-plane"></i>';
        
        // Scroll to bottom
        chatMessages.scrollTop = chatMessages.scrollHeight;
    }

    addChatMessage(message, sender, model = null) {
        const chatMessages = document.getElementById('chatMessages');
        const messageDiv = document.createElement('div');
        messageDiv.className = 'flex items-start space-x-3 mb-4';
        
        if (sender === 'user') {
            messageDiv.innerHTML = `
                <div class="bg-blue-600 text-white rounded-lg p-3 max-w-md ml-auto">
                    <p>${this.escapeHtml(message)}</p>
                </div>
                <div class="bg-blue-600 text-white rounded-full p-2 flex-shrink-0">
                    <i class="fas fa-user text-sm"></i>
                </div>
            `;
            messageDiv.classList.add('flex-row-reverse');
        } else {
            const formattedMessage = this.formatAIMessage(message);
            messageDiv.innerHTML = `
                <div class="bg-blue-500 text-white rounded-full p-2 flex-shrink-0">
                    <i class="fas fa-robot text-sm"></i>
                </div>
                <div class="bg-gray-100 rounded-lg p-3 max-w-2xl">
                    <div>${formattedMessage}</div>
                    ${model ? `<div class="text-xs text-gray-500 mt-2">Via: ${model}</div>` : ''}
                </div>
            `;
        }
        
        chatMessages.appendChild(messageDiv);
    }

    formatAIMessage(message) {
        // Convert line breaks and format lists
        return this.escapeHtml(message)
            .replace(/\n\n/g, '</p><p>')
            .replace(/\n/g, '<br>')
            .replace(/^/, '<p>')
            .replace(/$/, '</p>')
            .replace(/• /g, '<li>')
            .replace(/<li>/g, '</li><li>')
            .replace(/<\/li><li>([^<]*)<\/p>/g, '</li></ul><p>$1</p>')
            .replace(/<p><\/li>/g, '<ul>')
            .replace(/(<li>[^<]*)<br>/g, '$1</li>')
            .replace(/<li><\/li>/g, '');
    }

    escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }
}

// Initialize the application
const employeeManager = new EmployeeManager();
