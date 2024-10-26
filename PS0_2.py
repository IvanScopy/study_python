import numpy as np

# Hàm mục tiêu cần tối ưu
def objective(variables):
    x, y, z, q = variables  # Gán các giá trị trong mảng variables cho x, y, z, q
    return abs(3*x + 2*y + z + q - 34)  # Tính sai số giữa vế trái và 34

# Lớp đại diện cho mỗi hạt trong bầy đàn
class Particle:
    def __init__(self, bounds):
        self.pos = np.random.uniform(bounds[0], bounds[1], 4)  # Vị trí ngẫu nhiên
        self.vel = np.random.uniform(-1, 1, 4)  # Vận tốc ngẫu nhiên
        self.best_pos = self.pos.copy()  # Vị trí tốt nhất của hạt
        self.best_val = objective(self.pos)  # Giá trị tốt nhất tương ứng với vị trí tốt nhất
        self.cur_val = self.best_val  # Giá trị hiện tại của hàm mục tiêu

    def update_vel(self, global_best_pos, w, c1, c2):
        r1, r2 = np.random.rand(2)
        cog = c1 * r1 * (self.best_pos - self.pos)  # Thành phần nhận thức (cognitive)
        soc = c2 * r2 * (global_best_pos - self.pos)  # Thành phần xã hội (social)
        self.vel = w * self.vel + cog + soc  # Cập nhật vận tốc

    def update_pos(self, bounds):
        self.pos += self.vel  # Cập nhật vị trí bằng cách cộng vận tốc vào vị trí hiện tại
        self.pos = np.clip(self.pos, bounds[0], bounds[1])  # Giữ vị trí trong khoảng tìm kiếm

    def evaluate(self):
        self.cur_val = objective(self.pos)  # Tính giá trị tại vị trí hiện tại
        if self.cur_val < self.best_val:  # Nếu giá trị hiện tại tốt hơn giá trị tốt nhất đã biết
            self.best_val = self.cur_val  # Cập nhật giá trị tốt nhất
            self.best_pos = self.pos.copy()  # Cập nhật vị trí tốt nhất

# Thuật toán PSO chính
def pso(num_particles, bounds, num_iters, w=0.5, c1=1.5, c2=1.5):
    swarm = [Particle(bounds) for _ in range(num_particles)]  # Tạo bầy hạt
    global_best_pos = np.random.uniform(bounds[0], bounds[1], 4)  # Khởi tạo vị trí tốt nhất toàn cục ngẫu nhiên
    global_best_val = float('inf')  # Khởi tạo giá trị tốt nhất toàn cục với vô cực

    # Lưu trữ fitness của từng thế hệ
    generation_fitness = []

    for gen in range(num_iters):  # Lặp qua các thế hệ
        for particle in swarm:
            particle.evaluate()  # Đánh giá mỗi hạt
            if particle.best_val < global_best_val:  # Cập nhật giá trị tốt nhất toàn cục nếu cần
                global_best_val = particle.best_val
                global_best_pos = particle.best_pos.copy()

        for particle in swarm:
            particle.update_vel(global_best_pos, w, c1, c2)  # Cập nhật vận tốc mỗi hạt
            particle.update_pos(bounds)  # Cập nhật vị trí mỗi hạt

        # Lưu trữ giá trị fitness tốt nhất cho thế hệ này
        generation_fitness.append(global_best_val)
        print(f"Generation {gen+1}, Best Fitness: {global_best_val}")  # Hiển thị fitness của thế hệ hiện tại

        if global_best_val == 0:  # Nếu tìm thấy nghiệm chính xác, dừng sớm
            break

    return global_best_pos, global_best_val, generation_fitness

# Chạy PSO
bounds = [-100, 100]  # Giới hạn tìm kiếm cho các biến x, y, z, q
best_pos, best_val, gen_fitness = pso(num_particles=30, bounds=bounds, num_iters=10)

# Hiển thị kết quả
x, y, z, q = best_pos
print(f"\nGiá trị tối ưu: x = {x}, y = {y}, z = {z}, q = {q}")
print(f"Độ lệch với phương trình gốc: {best_val}")

# In ra fitness của tất cả các thế hệ
print("\nFitness của từng thế hệ:")
for i, fitness in enumerate(gen_fitness, start=1):
    print(f"Thế hệ {i}: {fitness}")
