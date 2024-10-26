import numpy as np

# Định nghĩa hàm mục tiêu
def objective_function(variables):
    x, y, z, q = variables
    return abs(3*x + 2*y + z + q - 34)  # Độ lệch giữa vế trái của phương trình và 34

# Lớp đại diện cho từng hạt (particle)
class Particle:
    def __init__(self, bounds):
        # Khởi tạo vị trí và vận tốc ngẫu nhiên
        self.position = np.random.uniform(bounds[0], bounds[1], 4)  # Vị trí chứa 4 biến: x, y, z, q
        self.velocity = np.random.uniform(-1, 1, 4)  # Vận tốc ngẫu nhiên
        self.best_position = self.position.copy()  # Vị trí tốt nhất của hạt
        self.best_value = objective_function(self.position)  # Giá trị hàm mục tiêu tốt nhất
        self.current_value = self.best_value

    def update_velocity(self, global_best_position, w, c1, c2):
        r1, r2 = np.random.rand(2)
        cognitive_component = c1 * r1 * (self.best_position - self.position)
        social_component = c2 * r2 * (global_best_position - self.position)
        self.velocity = w * self.velocity + cognitive_component + social_component

    def update_position(self, bounds):
        self.position += self.velocity
        # Giới hạn vị trí của hạt trong khoảng cho trước
        self.position = np.clip(self.position, bounds[0], bounds[1])

    def evaluate(self):
        self.current_value = objective_function(self.position)
        if self.current_value < self.best_value:
            self.best_value = self.current_value
            self.best_position = self.position.copy()

# Thuật toán PSO chính
def pso(num_particles, bounds, num_iterations, w=0.5, c1=1.5, c2=1.5):
    swarm = [Particle(bounds) for _ in range(num_particles)]
    global_best_position = np.random.uniform(bounds[0], bounds[1], 4)  # Không gian chứa 4 biến
    global_best_value = float('inf')

    for _ in range(num_iterations):
        for particle in swarm:
            particle.evaluate()
            if particle.best_value < global_best_value:
                global_best_value = particle.best_value
                global_best_position = particle.best_position.copy()

        for particle in swarm:
            particle.update_velocity(global_best_position, w, c1, c2)
            particle.update_position(bounds)

        # Kiểm tra nếu tìm được nghiệm chính xác
        if global_best_value == 0:
            break

    return global_best_position, global_best_value

# Chạy PSO để giải phương trình
bounds = [-10, 10]  # Giới hạn tìm kiếm cho các biến x, y, z, q
best_position, best_value = pso(num_particles=30, bounds=bounds, num_iterations=10)

# Hiển thị kết quả
x, y, z, q = best_position
print(f"Giá trị tối ưu: x = {x}, y = {y}, z = {z}, q = {q}")
print(f"Độ lệch với phương trình gốc: {best_value}")
