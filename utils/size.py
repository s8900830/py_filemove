class size_change:
    def size(input_str=''):
        if input_str is None:
            return False
        
        size_str = input_str.lower()
        if 'kb' in size_str:
            r_size = float(size_str.replace('kb', '').strip()) * 1024
        elif 'mb' in size_str:
            r_size = float(size_str.replace('mb', '').strip()) * 1024 * 1024 
        elif 'gb' in size_str:
            r_size = float(size_str.replace('gb', '').strip()) * 1024 * 1024 * 1024
        else:
            return int(input_str)

        return int(r_size)