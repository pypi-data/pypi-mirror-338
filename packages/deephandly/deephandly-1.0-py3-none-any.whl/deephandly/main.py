class handly:
    @staticmethod
    def mean(numbers):
        return sum(numbers) / len(numbers)

    @staticmethod
    def median(numbers):
        numbers.sort()
        n = len(numbers)
        mid = n // 2
        if n % 2 == 0:
            return (numbers[mid - 1] + numbers[mid]) / 2
        else:
            return numbers[mid]

    @staticmethod
    def mode(numbers):
        frequency = {}
        for num in numbers:
            frequency[num] = frequency.get(num, 0) + 1
        max_freq = max(frequency.values())
        modes = [num for num, freq in frequency.items() if freq == max_freq]
        return min(modes)  # Choose the smallest number if multiple modes exist

    @staticmethod
    def multimode(numbers):
        if not numbers:
            raise ValueError("The data list is empty.")
        frequency = {}
        for num in numbers:
            frequency[num] = frequency.get(num, 0) + 1
        max_freq = max(frequency.values())
        return [key for key, val in frequency.items() if val == max_freq]  # Return all modes
    


    @staticmethod
    def centrality(data):
        # Calculate Mean
        mean = sum(data) / len(data)
        
        # Calculate Median
        sorted_data = sorted(data)
        n = len(sorted_data)
        if n % 2 == 1:
            median = sorted_data[n // 2]
        else:
            median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
        
        # Calculate Mode and Multimode
        frequency = {}
        for num in data:
            frequency[num] = frequency.get(num, 0) + 1
        
        max_freq = max(frequency.values())
        modes = [key for key, value in frequency.items() if value == max_freq]
        smallest_mode = min(modes)  # Smallest mode
        
        return {
            "Mean": mean,
            "Median": median,
            "Mode": smallest_mode,
            "Multimode": modes
        }
    
    ## Mean + Median
    @staticmethod
    def mean_median(data):
        # Calculate Mean
        mean = sum(data) / len(data)
        
        # Calculate Median
        sorted_data = sorted(data)
        n = len(sorted_data)
        if n % 2 == 1:
            median = sorted_data[n // 2]
        else:
            median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
        
        return {
            "Mean": mean,
            "Median": median
        }
    
    
    ## Mean + Mode

    @staticmethod
    def mean_mode(data):
        # Calculate Mean
        mean = sum(data) / len(data)
        
        # Calculate Mode
        frequency = {}
        for num in data:
            frequency[num] = frequency.get(num, 0) + 1
        
        max_freq = max(frequency.values())
        modes = [key for key, value in frequency.items() if value == max_freq]
        smallest_mode = min(modes)  # Smallest mode
        
        return {
            "Mean": mean,
            "Mode": smallest_mode
        }
    
    ## Mean + MultiMode
    
    @staticmethod
    def mean_multimode(data):
        if not data:
            raise ValueError("The data list is empty.")
        
        mean = sum(data) / len(data)
        
        frequency = {}
        for num in data:
            frequency[num] = frequency.get(num, 0) + 1
        max_freq = max(frequency.values())
        modes = sorted([key for key, val in frequency.items() if val == max_freq])  # Sort modes in ascending order
        
        return f"Mean: {round(mean, 1)}\nMultiModes: {modes}"
    

    # Median + Mean
    @staticmethod
    def median_mean(data):
        if not data:
            raise ValueError("The data list is empty.")
        
        mean = sum(data) / len(data)
        sorted_data = sorted(data)
        n = len(sorted_data)
        median = (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2 if n % 2 == 0 else sorted_data[n//2]
        
        return f"Median: {median}\nMean: {mean}"
    

    @staticmethod
    def median_mode(data):
        if not data:
            raise ValueError("The data list is empty.")
        
        sorted_data = sorted(data)
        n = len(sorted_data)
        median = (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2 if n % 2 == 0 else sorted_data[n//2]
        
        frequency = {}
        for num in data:
            frequency[num] = frequency.get(num, 0) + 1
        max_freq = max(frequency.values())
        modes = sorted([key for key, val in frequency.items() if val == max_freq])  # Sort modes to get the smallest first
        mode = modes[0]  # Always return the smallest mode
        
        return f"Median: {median}\nMode: {mode}"
    

    @staticmethod
    def median_multimode(data):
        if not data:
            raise ValueError("The data list is empty.")
        
        sorted_data = sorted(data)
        n = len(sorted_data)
        median = (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2 if n % 2 == 0 else sorted_data[n//2]
        
        frequency = {}
        for num in data:
            frequency[num] = frequency.get(num, 0) + 1
        max_freq = max(frequency.values())
        modes = sorted([key for key, val in frequency.items() if val == max_freq])  # Sort modes in ascending order
        
        return f"Median: {round(median, 1)}\nMultiModes: {modes}"
    

        ## Mode + Mean

    @staticmethod
    def mode_mean(data):
        if not data:
            raise ValueError("The data list is empty.")
        
        mean = sum(data) / len(data)
        
        frequency = {}
        for num in data:
            frequency[num] = frequency.get(num, 0) + 1
        max_freq = max(frequency.values())
        modes = sorted([key for key, val in frequency.items() if val == max_freq])  # Sort modes to get the smallest first
        mode = modes[0]  # Always return the smallest mode
        
        return f"Mode: {mode}\nMean: {round(mean, 1)}"
    

    ## Mode + Median

    @staticmethod
    def mode_median(data):
        if not data:
            raise ValueError("The data list is empty.")
        
        sorted_data = sorted(data)
        n = len(sorted_data)
        median = (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2 if n % 2 == 0 else sorted_data[n//2]
        
        frequency = {}
        for num in data:
            frequency[num] = frequency.get(num, 0) + 1
        max_freq = max(frequency.values())
        modes = sorted([key for key, val in frequency.items() if val == max_freq])  # Sort modes to get the smallest first
        mode = modes[0]  # Always return the smallest mode
        
        return f"Mode: {mode}\nMedian: {round(median, 1)}"
    
## MultiMode + Mean

    @staticmethod
    def multimode_mean(data):
        if not data:
            raise ValueError("The data list is empty.")
        
        mean = sum(data) / len(data)
        
        frequency = {}
        for num in data:
            frequency[num] = frequency.get(num, 0) + 1
        max_freq = max(frequency.values())
        modes = sorted([key for key, val in frequency.items() if val == max_freq])  # Sort modes in ascending order
        
        return f"MultiModes: {modes}\nMean: {round(mean, 1)}"


 ## MultiMode + Median

    @staticmethod
    def multimode_median(data):
        if not data:
            raise ValueError("The data list is empty.")
        
        sorted_data = sorted(data)
        n = len(sorted_data)
        median = (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2 if n % 2 == 0 else sorted_data[n//2]
        
        frequency = {}
        for num in data:
            frequency[num] = frequency.get(num, 0) + 1
        max_freq = max(frequency.values())
        modes = sorted([key for key, val in frequency.items() if val == max_freq])  # Sort modes in ascending order
        
        return f"MultiModes: {modes}\nMedian: {round(median, 1)}"
    

## Range Method
    @staticmethod
    def range(numbers):
        if not numbers:
            return None  # Return None if the list is empty
        return max(numbers) - min(numbers)



    @staticmethod
    def sample_variance(numbers):
        if len(numbers) < 2:
            return None  # Variance requires at least two data points
        mean_value = handly.mean(numbers)
        return sum((x - mean_value) ** 2 for x in numbers) / (len(numbers) - 1)
    
    @staticmethod
    def population_variance(numbers):
        if not numbers:
            return None  # Population variance requires at least one data point
        mean_value = handly.mean(numbers)
        return sum((x - mean_value) ** 2 for x in numbers) / len(numbers)
    


## Standard Deviation Method
    @staticmethod
    def sample_std(numbers):
        variance = handly.sample_variance(numbers)
        return variance ** 0.5 if variance is not None else None
    
    @staticmethod
    def population_std(numbers):
        variance = handly.population_variance(numbers)
        return variance ** 0.5 if variance is not None else None


##### Leap Year Method
    @staticmethod
    def is_leap_year(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

