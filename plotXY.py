
class PlotXY():

    def refleshPlot(self, model, plotWidget):
        
        # 合計時間を計算
        def calicurateTimeAndVelocity(distance, acceleration):
            time = ( 2.0 * distance / acceleration )**0.5 # 面積(距離)と角度(加速度)で時間(底辺)を直角三角形の三角関数で計算
            velocity = time * acceleration # 速度は時間*加速度
            return time, velocity
        
        def calicurateTimeAndVelocityArray(position_array, a, v_max):
            d_max = 0.5 * a * v_max**2.0 # 最高速に達する距離[m]
            v_arr = [0.0] # m/s
            t_arr = [0.0] # s
            for i in range( len(position_array) )[:-1]:
                x_def = abs(position_array[i+1] - position_array[i])

                # 台形駆動か = 2点の移動距離の差を2で割った値が最高速に達する距離より大きいか
                if x_def / 2.0 > d_max:
                    accelarate_distance = d_max
                    deaccelarate_distance = d_max
                    constant_distance = x_def - d_max * 2.0
                else:
                    # 三角駆動の場合 加速時間と減速時間は2点の移動距離を2で割った値
                    accelarate_distance = x_def / 2.0
                    deaccelarate_distance = x_def / 2.0
                    constant_distance = 0.0
                
                # 等加速度(加速)
                t, v = calicurateTimeAndVelocity(accelarate_distance, a)
                t_arr.append(t + t_arr[-1])
                v_arr.append(v_arr[-1] + v)
                
                # 等速度
                t_arr.append( constant_distance / v_arr[-1] + t_arr[-1] )
                v_arr.append( v_arr[-1] )
                
                # 等加速度(減速)
                t, v = calicurateTimeAndVelocity(deaccelarate_distance, a)
                t_arr.append(t + t_arr[-1])
                v_arr.append(v_arr[-1] - v)
            return t_arr, v_arr
        
        # モデルのアイテムから座標を取得データがない場合は0.0とする
        coordinates = { 'X':[], 'Y':[], 'Z':[] }
        for axis in coordinates:
            coordinates[axis] = [ self.toFloat( item.get(axis) ) for item in model.items ]
        
        # xyz位置のグラフにすべての点をプロット
        plotWidget['position_xyz'].clear()
        plotWidget['position_xyz'].plot(coordinates['X'], coordinates['Y'])

        # xのt-v線図をプロット
        for axis in coordinates:
            try:
                plotWidget['position_' + axis].clear()
                times, velocities = calicurateTimeAndVelocityArray(coordinates[axis], 10.0, 1.0)
                plotWidget['position_' + axis].plot(times, velocities)
            except:
                pass
        
    def toFloat(self, str_):
        try:
            return float(str_)
        except:
            return 0.0