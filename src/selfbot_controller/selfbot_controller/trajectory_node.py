#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry, Path
from geometry_msgs.msg import PoseStamped

class TrajectoryPublisher(Node):
    def __init__(self):
        super().__init__('trajectory_publisher')
        
        # 1. Configurar el Subscriber
        # Se suscribe al topic de odometría
        self.subscription = self.create_subscription(
            Odometry,
            '/selfbot_controller/odom',
            self.odom_callback,
            10
        )
        
        # 2. Configurar el Publisher
        # Publicará el Path completo en este topic
        self.publisher_ = self.create_publisher(
            Path, 
            '/selfbot_controller/trajectory', 
            10
        )
        
        # 3. Inicializar el mensaje Path
        self.path_msg = Path()
        
        self.get_logger().info('Nodo TrajectoryPublisher iniciado. Esperando odometría...')

    def odom_callback(self, odom_msg):
        # Aseguramos que el Path tenga el mismo frame que la odometría (ej. "odom")
        if not self.path_msg.header.frame_id:
            self.path_msg.header.frame_id = odom_msg.header.frame_id

        # Actualizamos el timestamp del Path al tiempo actual
        self.path_msg.header.stamp = self.get_clock().now().to_msg()

        # Creamos un PoseStamped a partir de la odometría recibida
        pose = PoseStamped()
        
        # Copiamos el header de la odometría (para mantener el tiempo exacto de esa lectura)
        pose.header = odom_msg.header
        
        # Copiamos la posición y orientación
        pose.pose = odom_msg.pose.pose

        # 4. Almacenar la pose en la lista del Path
        self.path_msg.poses.append(pose)

        # 5. Publicar el Path actualizado
        self.publisher_.publish(self.path_msg)

def main(args=None):
    rclpy.init(args=args)
    node = TrajectoryPublisher()
    
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()