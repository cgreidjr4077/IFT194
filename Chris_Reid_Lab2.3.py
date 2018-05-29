import math

n_reps = 100

n_extra_reps = 25

n_pages = 20

n_papers_box = 200

n_req_papers = (n_reps + n_extra_reps) * n_pages

n_req_boxes = math.ceil(n_req_papers / n_papers_box)

print("The number of required paper boxes = ", n_req_boxes)
