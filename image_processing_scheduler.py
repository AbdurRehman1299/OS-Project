#Get number of images
n = int(input("Enter number of images: "))

#Input each image
images = []
for i in range(n):
	img_id = input(f"Enter ImageID for Image {i+1}: ")
	arrival = int(input(f"Enter arrival time for Image {i+1}: "))
	burst = int(input(f"Enter burst time for Image {i+1}: "))
	images.append({
		"img_id": img_id,
		"arrival_time": arrival,
		"burst_time": burst,
		"completion_time": 0,
		"turnaround_time": 0,
		"waiting_time": 0,
		"completed": False
	})

#Sort images by arrival time
images.sort(key=lambda x: x["arrival_time"])

#Initialize variables
current_time = 0
completed = 0

#SJF Non-Preemptive Scheduling
while completed < n:
	#Get available and not yet completed images
	available = [img for img in images if img["arrival_time"] <= current_time and not img["completed"]]

	if available:
		#Select image with shortest burst time
		short_job_image = min(available, key=lambda x: x["burst_time"])

		#Compute timing details
		current_time += short_job_image["burst_time"]
		short_job_image["completion_time"] = current_time
		short_job_image["turnaround_time"] = short_job_image["completion_time"] - short_job_image["arrival_time"]
		short_job_image["waiting_time"] = short_job_image["turnaround_time"] - short_job_image["burst_time"]
		short_job_image["completed"] = True

		completed += 1
	else:
		current_time += 1	#If no image is available, increase time


#Print table
print("\n" + "-"*65)
print("ImageID | Arrival | Burst | Completion | Turnaround | Waiting")
print("-"*65)

#Sort back the images
images.sort(key=lambda x: x["img_id"])

for img in images:
    print(f"{img['img_id']:>7} |"
          f"{img['arrival_time']:>8} |"
          f"{img['burst_time']:>6} |"
          f"{img['completion_time']:>11} |"
          f"{img['turnaround_time']:>11} |"
          f"{img['waiting_time']:>8}")

print("-"*65)

avg_tat = sum(img["turnaround_time"] for img in images) / n
avg_wt = sum(img["waiting_time"] for img in images) / n

print(f"\nAverage Turnaround Time: {avg_tat:.2f}")
print(f"Average Waiting Time: {avg_wt:.2f}")