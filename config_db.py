import sqlite3

class ConfigDB:
    def __init__(self):
        self.db_file = "db_file.db"
        self.connection = sqlite3.connect(self.db_file)
        self.cursor = self.connection.cursor()
        self.create_table()
    def delete_table(self):
        self.cursor.execute("DROP TABLE config_db")
        
    def create_table(self):
        
        query = '''
            CREATE TABLE IF NOT EXISTS config_db (
                ConfigName TEXT NOT NULL PRIMARY KEY,
                ConfigValue TEXT NOT NULL
            )
        '''
        self.cursor.execute(query)
        self.connection.commit()


    def set_led_color(self, default_light_color):
        #ConfigName = "default_light_color"
        #ConfigValue ={r:100,g:0,b:0}
        #if not exist insert else update
        if self.get_led_color():
            self.cursor.execute("UPDATE config_db  SET ConfigValue = ? WHERE ConfigName = 'default_light_color'", (default_light_color,))
        else:
            self.cursor.execute("INSERT INTO config_db (ConfigName, ConfigValue) VALUES (?, ?)", ("default_light_color", default_light_color))
        self.connection.commit()
        
    def set_speech_speed(self, speech_speed):
        #ConfigName = "speech_speed"
        #ConfigValue = 0.5
        #if not exist insert else update
        if self.get_speech_speed():
            self.cursor.execute("UPDATE config_db  SET ConfigValue = ? WHERE ConfigName = 'speech_speed'", (speech_speed,))
        else:  
            self.cursor.execute("INSERT INTO config_db (ConfigName, ConfigValue) VALUES (?, ?)", ("speech_speed", speech_speed))
        self.connection.commit()

            
    def get_all_config(self):
        query = '''
         SELECT * FROM config_db
         '''
        self.cursor.execute(query)
        return self.cursor.fetchall()
    def get_led_color(self):
        color = None
        query = '''
         SELECT ConfigValue FROM config_db WHERE ConfigName = "default_light_color"
         '''
        try:
            self.cursor.execute(query)
            color = self.cursor.fetchone()
            return color[0] if color else None
        except Exception as e:
            return None
        
    def get_speech_speed(self):
        speed = None
        query = '''
         SELECT ConfigValue FROM config_db WHERE ConfigName = "speech_speed"
         '''
        try:
            self.cursor.execute(query)
            speed = self.cursor.fetchone()
            return speed[0] if speed else None
        except Exception as e:
            return None

    def close_connection(self):
        self.connection.close()

# 使用示例
if __name__ == '__main__':
    db = ConfigDB()
    # 设置配置
    # db.set_led_color("{'r':100,'g':0,'b':0}")
    # db.set_speech_speed(0.5)    