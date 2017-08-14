
���Y�
  �               @   s*   d  d l  m Z Gd d �  d e � Z d S)�   )�TLObjectc                   s�   e  Z d  Z d Z d Z d Z �  f d d �  Z d d �  Z d d	 �  Z e	 d
 d �  � Z
 d d �  Z d d �  Z d d �  Z d d �  Z �  S)�0ChannelAdminLogEventActionParticipantToggleAdminz�Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    channelAdminLogEventActionParticipantToggleAdmin#d5676710 prev_participant:ChannelParticipant new_participant:ChannelParticipant = ChannelAdminLogEventActionl   g�* l   �se c                s#   t  �  j �  | |  _ | |  _ d S)a.  
        :param prev_participant: Telegram type: "ChannelParticipant".
        :param new_participant: Telegram type: "ChannelParticipant".

        Constructor for ChannelAdminLogEventAction: Instance of either ChannelAdminLogEventActionChangeTitle, ChannelAdminLogEventActionChangeAbout, ChannelAdminLogEventActionChangeUsername, ChannelAdminLogEventActionChangePhoto, ChannelAdminLogEventActionToggleInvites, ChannelAdminLogEventActionToggleSignatures, ChannelAdminLogEventActionUpdatePinned, ChannelAdminLogEventActionEditMessage, ChannelAdminLogEventActionDeleteMessage, ChannelAdminLogEventActionParticipantJoin, ChannelAdminLogEventActionParticipantLeave, ChannelAdminLogEventActionParticipantInvite, ChannelAdminLogEventActionParticipantToggleBan, ChannelAdminLogEventActionParticipantToggleAdmin.
        N)�super�__init__�prev_participant�new_participant)�selfr   r   )�	__class__� �t/home/cluster/Desktop/Telethon-Explorer/telethon/tl/types/channel_admin_log_event_action_participant_toggle_admin.pyr      s    	z9ChannelAdminLogEventActionParticipantToggleAdmin.__init__c             C   sL   d |  j  d  k r d  n |  j  j �  d |  j d  k r< d  n |  j j �  i S)Nr   r   )r   �to_dictr   )r   r
   r
   r   r      s    $z8ChannelAdminLogEventActionParticipantToggleAdmin.to_dictc             C   s:   | j  t j d d �|  j j | � |  j j | � d  S)N�signedF)�	write_intr   �constructor_idr   �on_sendr   )r   �writerr
   r
   r   r      s    z8ChannelAdminLogEventActionParticipantToggleAdmin.on_sendc               C   s   t  d d � S)z-Returns an "empty" instance (attributes=None)N)r   r
   r
   r
   r   �empty$   s    z6ChannelAdminLogEventActionParticipantToggleAdmin.emptyc             C   s"   | j  �  |  _ | j  �  |  _ d  S)N)�tgread_objectr   r   )r   �readerr
   r
   r   �on_response)   s    z<ChannelAdminLogEventActionParticipantToggleAdmin.on_responsec             C   s   d S)Nz�channelAdminLogEventActionParticipantToggleAdmin#d5676710 prev_participant:ChannelParticipant new_participant:ChannelParticipant = ChannelAdminLogEventActionr
   )r   r
   r
   r   �__repr__-   s    z9ChannelAdminLogEventActionParticipantToggleAdmin.__repr__c             C   s   t  j |  � S)N)r   �pretty_format)r   r
   r
   r   �__str__0   s    z8ChannelAdminLogEventActionParticipantToggleAdmin.__str__c             C   s   t  j |  d d �S)N�indent�    )r   r   )r   r
   r
   r   �	stringify3   s    z:ChannelAdminLogEventActionParticipantToggleAdmin.stringify)�__name__�
__module__�__qualname__�__doc__r   �subclass_of_idr   r   r   �staticmethodr   r   r   r   r   r
   r
   )r	   r   r      s   r   N)Ztl.tlobjectr   r   r
   r
   r
   r   �<module>   s   